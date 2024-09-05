import os
import pandas as pd

python_directory = './Datasets/QuixBugs/python_programs'  
python_output= 'QuixBugs_Extracted/ExtractedPythonQuixBugs.csv'
python_correct_directory = './Datasets/QuixBugs/correct_python_programs'  
java_directory = './Datasets/QuixBugs/java_programs'
java_output = 'QuixBugs_Extracted/ExtractedJavaQuixBugs.csv'
java_correct_directory = './Datasets/QuixBugs/correct_java_programs'

# extracts the code and comments from the Quixbugs python files
def extract_python_code_and_context(file_content):
    code_lines = []
    comment_lines = []
    in_comment_block = False

    for line in file_content.splitlines():
        stripped_line = line.strip()
        if stripped_line.startswith('"""'):
            in_comment_block = not in_comment_block
            if in_comment_block:
                comment_lines.append(stripped_line[3:].strip()) # removes the quotes from the comment at the beginning
            else:
                comment_lines.append(stripped_line[:-3].strip()) # removes the quotes from the comment at the end
        elif in_comment_block:
            comment_lines.append(stripped_line) # extracts the comment from the comment block
        else:
            code_lines.append(line) # extracts the code

    return "\n".join(code_lines), "\n".join(comment_lines) # adds a newline to maintain the format of the original code and comments

# extracts the code from the Quixbugs java files
def extract_java_code(file_content):
    code_lines = []
    in_comment_block = False

    for line in file_content.splitlines():
        stripped_line = line.strip()
        if stripped_line.startswith("/*"):
            in_comment_block = True
        if not in_comment_block and not stripped_line.startswith("//"):
            code_lines.append(line)
        if stripped_line.endswith("*/"):
            in_comment_block = False

    return "\n".join(code_lines)

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

python_data = []
java_data = []
python_correct_data = []
java_correct_data = []
code_context = []

for filename in os.listdir(python_directory):
    if filename.endswith('.py'):
        file_path = os.path.join(python_directory, filename)
        content = read_file_content(file_path)
        code, context = extract_python_code_and_context(content)
        python_data.append([filename, code, context])

for filename in os.listdir(python_correct_directory):
    if filename.endswith('.py'):
        file_path = os.path.join(python_correct_directory, filename)
        content = read_file_content(file_path)
        python_correct_code, context_correct = extract_python_code_and_context(content)
        python_correct_data.append([python_correct_code])

context_index = 0

for filename in os.listdir(java_directory):
    if filename.endswith('.java'):
        file_path = os.path.join(java_directory, filename)
        content = read_file_content(file_path)
        code = extract_java_code(content)
        
        if context_index < len(code_context):
            context = code_context[context_index]
        else:
            context = "Error"
        
        java_data.append([filename, code, context])
        context_index += 1

for filename in os.listdir(java_correct_directory):
    if filename.endswith('.java'):
        file_path = os.path.join(java_correct_directory, filename)
        content = read_file_content(file_path)
        java_correct_code = extract_java_code(content)
        java_correct_data.append([java_correct_code])

# NOTE: The Java dataset has an additional two files that are extracted. 
# These files aren't present in the Python dataset and it therefore causes 
# some of the corresponding contexts and correct code to be incorrectly placed.

df_python = pd.DataFrame(python_data, columns=['Filename', 'Code', 'Context and Comments'])
df_python_correct = pd.DataFrame(python_correct_data, columns=['Correct Code'])
df_python_combined = pd.concat([df_python, df_python_correct], axis=1)
df_python_combined.to_csv(python_output, index=False, encoding='utf-8')

df_java = pd.DataFrame(java_data, columns=['Filename', 'Code', 'Context and Comments'])
df_java_correct = pd.DataFrame(java_correct_data, columns=['Correct Code'])
df_java_combined = pd.concat([df_java, df_java_correct], axis=1)
df_java_combined.to_csv(java_output, index=False, encoding='utf-8')

