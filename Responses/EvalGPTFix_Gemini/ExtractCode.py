import pandas as pd
import os

# Read the CSV file
csv_file = 'Responses/EvalGPTFix_Gemini/Gemini_1.5_Pro_EvalGPTFix.csv'
df = pd.read_csv(csv_file)

# Extract the directory from the CSV file path
csv_directory = os.path.dirname(csv_file)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    file_name = row['File Name']
    
    # Skip the row if the file name is 'file_6'
    if file_name == 'file_6':
        continue
    
    fixed_code = row['fixed code']
    
    # Handle NaN values and ensure fixed_code is a string
    if pd.isna(fixed_code):
        fixed_code = ""
    else:
        fixed_code = str(fixed_code)
    
    # Create a text file named "FileName.txt"
    text_file_name = f"{file_name}.txt"
    
    # Ensure the "Code" directory exists within the CSV file's directory
    code_directory = os.path.join(csv_directory, 'Code')
    if not os.path.exists(code_directory):
        os.makedirs(code_directory)
    
    # Write the "Fixed Code" content to the text file in the "Code" directory
    text_file_path = os.path.join(code_directory, text_file_name)
    with open(text_file_path, 'w') as text_file:
        text_file.write(fixed_code)

print("Fixed code content has been extracted and saved to text files.")