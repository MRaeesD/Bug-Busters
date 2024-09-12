import os
import pandas as pd
import requests
from dotenv import load_dotenv
import re
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

input_csv_1 = './QuixBugs_Extracted/ExtractedJavaQuixBugs-APR.csv'
output_csv_1 = './Responses/QuixBugs_GEMINI/APR/APR_zero_shot_Gemini_1.5_Pro_Java.csv'
output_csv_2 = './Responses/QuixBugs_GEMINI/APR/APR_one_shot_Gemini_1.5_Pro_Java.csv'

base_prompt = '''Please correct the bug in the above Java code snippet and provide a reason for the fix. 
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

data_zs = []
data_os = []

df_input1 = pd.read_csv(input_csv_1)

for index, col in df_input1.iterrows():
    file_name = col[0]
    code_content = col[1]
    explanation = col[2]
    correction = col[4]

    print(f"Processing file: {file_name} \n")

    zero_shot_prompt = 'Code:' + code_content + '\nLine of Code with bug: ' + correction +'\n\n'+ base_prompt
    one_shot_prompt = 'Code: ' + code_content + '\nThe code is expected to function as follows: ' + explanation +  '\nLine of Code with bug: ' + correction + '\n\n' + base_prompt 

    # zero-shot prompting
    gemini_response_zs, input_tokens_zs, output_tokens_zs = prompt_gemini(zero_shot_prompt)
    reason_zs, fix_zs = parse_response(gemini_response_zs)
    data_zs.append([file_name, zero_shot_prompt, gemini_response_zs, input_tokens_zs, output_tokens_zs, reason_zs, fix_zs])

    # one-shot prompting
    gemini_response_os, input_tokens_os, output_tokens_os = prompt_gemini(one_shot_prompt)
    reason_os, fix_os = parse_response(gemini_response_os)
    data_os.append([file_name, one_shot_prompt, gemini_response_os, input_tokens_os, output_tokens_os, reason_os, fix_os])

    with open(f"./Responses/QuixBugs_Gemini/APR/Code/1.5_pro_java/Zs/1.5_pro_java_{file_name}", 'w') as file:
        file.write(fix_zs+"\n")
    
    with open(f"./Responses/QuixBugs_Gemini/APR/Code/1.5_pro_java/Os/1.5pro_java_{file_name}", 'w') as file:
        file.write(fix_os+"\n")

df_output_zs = pd.DataFrame(data_zs, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used',
    'Reason', 'Proposed Code Fix'
])

df_output_os = pd.DataFrame(data_os, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used',
    'Reason', 'Proposed Code Fix'
])

df_output_zs.to_csv(output_csv_1, index=False)
df_output_os.to_csv(output_csv_2, index=False)

