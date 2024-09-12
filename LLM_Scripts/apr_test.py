import os
import pandas as pd
import requests
from dotenv import load_dotenv
import re

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

input_csv_1 = './QuixBugs_Extracted/ExtractedPythonQuixBugs.csv'
input_csv_2 = './Responses/QuixBugs_GPT/test_zero_shot_ChatGPT_4o_Mini_Python.csv'
output_csv_1 = './Responses/QuixBugs_GPT/APR_test_zero_shot_ChatGPT_4o_Mini_Python.csv'
output_csv_2 = './Responses/QuixBugs_GPT/APR_test_one_shot_ChatGPT_4o_Mini_Python.csv'

base_prompt = '''Please correct the bug in the above Python code snippet and provide a reason for the fix. 
                \nIndicate the entire corrected code in the format:
                \nReason: <Reason for the fix> (skip a line after the reason)
                \nFix: <Rewritten corrected code with a comment indicating where the change is made>
                \nNote: Please do not add any additional comments after providing the fix.'''

def prompt_chatgpt(content):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": "gpt-4o-mini", 
        "messages": [{"role": "user", "content": content}],
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    response_json = response.json()
    
    message_content = response_json["choices"][0]["message"]["content"].strip()
    usage = response_json["usage"]
    input_tokens = usage["prompt_tokens"]
    output_tokens = usage["completion_tokens"]
    
    return message_content, input_tokens, output_tokens

def parse_response(response):
    lines = response.split('\n')
    reason_for_fix = lines[0].replace('Reason: ', '').strip()
    fix = '\n'.join(lines[3:]).replace('Fix: ', '').replace('```python', '').replace('```', '').strip()
    return reason_for_fix, fix

data_zs = []
data_os = []

df_input1 = pd.read_csv(input_csv_1)
df_input2 = pd.read_csv(input_csv_2)

for (index1, col1), (index2, col2) in zip(df_input1.iterrows(), df_input2.iterrows()):
    file_name = col1[0]
    code_content = col1[1]
    explanation = col1[2]
    correction = col2[15]

    print(f"Processing file: {file_name} \n")

    zero_shot_prompt = 'Code:' + code_content + '\nLine of Code with bug: ' + correction +'\n\n'+ base_prompt
    one_shot_prompt = 'Code: ' + code_content + '\nThe code is expected to function as follows: ' + explanation +  '\nLine of Code with bug: ' + correction + '\n\n' + base_prompt 

    # zero-shot prompting
    chatgpt_response_zs, input_tokens_zs, output_tokens_zs = prompt_chatgpt(zero_shot_prompt)
    reason_zs, fix_zs = parse_response(chatgpt_response_zs)
    data_zs.append([file_name, zero_shot_prompt, chatgpt_response_zs, input_tokens_zs, output_tokens_zs, reason_zs, fix_zs])

    # one-shot prompting
    chatgpt_response_os, input_tokens_os, output_tokens_os = prompt_chatgpt(one_shot_prompt)
    reason_os, fix_os = parse_response(chatgpt_response_os)
    data_os.append([file_name, zero_shot_prompt, chatgpt_response_os, input_tokens_os, output_tokens_os, reason_os, fix_os])

    with open(f"./Responses/Code/Zs/4o_mini_python_{file_name}", 'w') as file:
        file.write(fix_zs+"\n")
    
    with open(f"./Responses/Code/Os/4o_mini_python_{file_name}", 'w') as file:
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

