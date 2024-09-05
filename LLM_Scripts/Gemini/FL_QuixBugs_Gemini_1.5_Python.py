import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

input_csv = 'QuixBugs_Extracted/python_programs/ExtractedPythonQuixBugs.csv'
output_csv1 = './Responses/zero_shot_Gemini_1.5_Python.csv'
output_csv2 = './Responses/one_shot_Gemini_1.5_Python.csv'

prompt_test = '''Please locate the bug in the following Python code snippet. 
                \nOnly indicate the location of the bug and the reason it is a bug (without providing a fix) in the format: 
                \nLine Number: <Line number> (skip a line after the line number)
                \nLine of Code: <Line of code with the bug> (skip a line after the code line)
                \nReason: <Reason without a fix>'''

def prompt_gemini(content):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(content)
    return response.text.strip()

def parse_response(response):
    lines = response.split('\n')
    bug_line_number = lines[0].replace('Line Number: ', '').strip()
    buggy_line = lines[2].replace('Line of Code: ', '').strip()
    reason_for_bug = '\n'.join(lines[4:]).replace('Reason: ', '').strip()
    return bug_line_number, buggy_line, reason_for_bug

data_zs = []
data_os = []

df_input = pd.read_csv(input_csv)

for index, col in df_input.iterrows():
    file_name = col[0]
    code_content = col[1]
    explanation = col[2]
    
    zero_shot_prompt = prompt_test + '\n\nCode:\n' + code_content
    one_shot_prompt = prompt_test + '\n\n' + '\n\nCode Context:\n' + explanation + '\n\nCode:\n' + code_content

    # zero-shot prompting
    gemini_response_zs = prompt_gemini(zero_shot_prompt)
    bug_line_number_zs, buggy_line_zs, reason_for_bug_zs = parse_response(gemini_response_zs)
    data_zs.append([file_name, zero_shot_prompt, bug_line_number_zs, buggy_line_zs, reason_for_bug_zs])
    
    # one-shot prompting
    gemini_response_os = prompt_gemini(one_shot_prompt)
    bug_line_number_os, buggy_line_os, reason_for_bug_os = parse_response(gemini_response_os)
    data_os.append([file_name, one_shot_prompt, bug_line_number_os, buggy_line_os, reason_for_bug_os])

df_output_zs = pd.DataFrame(data_zs, columns=['File Name', 'Prompt', 'Bug Line Number', 'Code Line with Bug', 'Reason for Bug'])
df_output_os = pd.DataFrame(data_os, columns=['File Name', 'Prompt', 'Bug Line Number','Code Line with Bug', 'Reason for Bug'])

df_output_zs.to_csv(output_csv1, index=False)
df_output_os.to_csv(output_csv2, index=False)

