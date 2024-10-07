import os
import pandas as pd
import requests
from dotenv import load_dotenv
import re
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

input_csv = './EvalGPTFix_Extracted/ExtractedEvalGPTFix.csv'
output_csv2 = './Responses/EvalGPTFix_Gemini/Gemini_1.5_Pro_EvalGPTFix_Guided.csv'

base_prompt = '''Please correct the bug in the above Java code snippet and provide a reason for the fix. The location of the bug is commented.
                \nIndicate the entire corrected code in the format:
                \nReason: <Reason for the fix> (skip a line after the reason)
                \nFix: <Rewritten corrected code with a comment indicating where the change is made>
                \nNote: Please do not add any additional comments after providing the fix.'''

def prompt_gemini(content):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(content)
    message_content = response.text.strip()
    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count
    return message_content, input_tokens, output_tokens

def parse_response(response):
    lines = response.split('\n')
    reason_for_fix = lines[0].replace('Reason: ', '').strip()
    fix = '\n'.join(lines[3:]).replace('Fix: ', '').replace('```java', '').replace('```', '').strip()
    return reason_for_fix, fix

files_to_process = [
    "file_28", "file_31", "file_40", "file_41", "file_61", "file_79", "file_93", "file_99", "file_113", "file_125",
]


data_zs = []
data_os = []

df_input = pd.read_csv(input_csv, encoding = 'utf-8')

df_filtered = df_input[df_input.iloc[:, 0].isin(files_to_process)]

for index, col in df_input.iterrows():
    file_name = col[0]
    code_content = col[2]
    error_code = col[4]
    explanation = col[5]

    print(f"Processing {file_name}")

    # one-shot prompting
    if error_code == 'CE':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: There is a ' + explanation + ' in the code' + '\n\nCode:\n' + code_content
    elif error_code == 'TLE':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:\n' + code_content
    elif error_code == 'MLE':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:\n' + code_content
    elif error_code == 'RE':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:\n' + code_content
    elif error_code == 'WA':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: The output provides the ' + explanation + '\n\nCode:\n' + code_content

    # one-shot prompting
    gemini_response_os, input_tokens_os, output_tokens_os = prompt_gemini(one_shot_prompt)
    reason_for_fix, fixed_code_content  = parse_response(gemini_response_os)

    print(one_shot_prompt)

    print(f"reason for fix: {reason_for_fix}")

    print(f"fixed code: {fixed_code_content}")

    data_os.append([
        file_name, one_shot_prompt, gemini_response_os, input_tokens_os, output_tokens_os, reason_for_fix, fixed_code_content
    ])

    with open(f"Responses/EvalGPTFix_Gemini/Guided_Code/{file_name}.txt", 'w', encoding='utf-8') as file:
            file.write(fixed_code_content)

df_output_os = pd.DataFrame(data_os, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used', 'Reason for Fix', 'Fixed Code'
])

df_output_os.to_csv(output_csv2, index=False, encoding='utf-8')
