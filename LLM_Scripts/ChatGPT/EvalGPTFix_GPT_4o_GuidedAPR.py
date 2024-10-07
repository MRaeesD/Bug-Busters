import os
import pandas as pd
import requests
from dotenv import load_dotenv
import re

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

input_csv = './EvalGPTFix_Extracted/ExtractedEvalGPTFix.csv'
output_csv2 = './Responses/EvalGPTFix_GPT/ChatGPT_4o_EvalGPTFix_Guided.csv'

base_prompt = '''Please correct the bug in the above Java code snippet and provide a reason for the fix. The location of the bug is commented.
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
        "model": "gpt-4o", 
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
    fix = '\n'.join(lines[3:]).replace('Fix: ', '').replace('```java', '').replace('```', '').strip()
    return reason_for_fix, fix

'''
files_to_process = [
    "file_1", "file_2", "file_3", "file_4", "file_5", "file_6", "file_7", "file_8", "file_9", "file_10",
    "file_11", "file_12", "file_13", "file_14", "file_15", "file_16", "file_17", "file_18", "file_21",
    "file_23", "file_25", "file_26", "file_27", "file_28", "file_30", "file_31", "file_35", "file_36",
    "file_38", "file_39", "file_40"
]
'''
'''
files_to_process = [
    "file_6", "file_7", "file_19", "file_23", "file_28", "file_31", "file_40", "file_41", "file_42", "file_43",
    "file_49", "file_59", "file_61", "file_64", "file_66", "file_70", "file_71", "file_72", "file_73", "file_76",
    "file_78", "file_79", "file_89", "file_93", "file_99", "file_105", "file_110", "file_113", "file_116", "file_125",
    "file_126", "file_128", "file_130", "file_133", "file_135", "file_147"
]
'''

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
    chatgpt_response_os, input_tokens_os, output_tokens_os = prompt_chatgpt(one_shot_prompt)
    reason_for_fix, fixed_code_content  = parse_response(chatgpt_response_os)

    print(one_shot_prompt)

    print(f"reason for fix: {reason_for_fix}")

    print(f"fixed code: {fixed_code_content}")

    data_os.append([
        file_name, one_shot_prompt, chatgpt_response_os, input_tokens_os, output_tokens_os, reason_for_fix, fixed_code_content
    ])

    with open(f"Responses/EvalGPTFix_GPT/Guided_Code/{file_name}.txt", 'w', encoding='utf-8') as file:
            file.write(fixed_code_content)

df_output_os = pd.DataFrame(data_os, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used', 'Reason for Fix', 'Fixed Code'
])

df_output_os.to_csv(output_csv2, index=False, encoding='utf-8')
