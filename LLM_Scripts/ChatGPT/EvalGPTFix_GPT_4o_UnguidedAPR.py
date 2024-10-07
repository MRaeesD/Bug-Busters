import os
import pandas as pd
import requests
from dotenv import load_dotenv
import re

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

input_csv = './EvalGPTFix_Extracted/ExtractedEvalGPTFix.csv'
output_csv2 = './Responses/EvalGPTFix_GPT/ChatGPT_4o_EvalGPTFix_4.csv'

base_prompt = ''' Debug the following Java code snippet. Localise the bug(s), provide a fix for the bug(s) and a reason for the fix. 
Provide the full code snippet with the bugs fixed wrapped in a code block based on the following template structure:
    ```
        {
        "Fault Localisation": [
            {
            "Code": <Buggy code line>,
            "Reason": <Reason for the bug>
            },
            ...
        ]

        "Automatic Program Repair": [
            {
            "Fixed Code": <Fully fixed code, wrapped in a Java code block: ```java```. >,
            "Reason for Fix": <Reason for the fix>
            },
        ]
        }
    ```
'''

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

def parse_response(input_string):
    
    fault_localisation_pattern = re.compile(r'"Fault Localisation": \[(.*?)\],\s*"Automatic Program Repair"', re.DOTALL)
    automatic_program_repair_pattern = re.compile(r'"Automatic Program Repair": \[(.*?)\]\s*}', re.DOTALL)
    fixed_code_pattern = re.compile(r'"Fixed Code":\s*```java(.*?)```', re.DOTALL)
    
    fault_localisation_matches = fault_localisation_pattern.search(input_string)
    automatic_program_repair_matches = automatic_program_repair_pattern.search(input_string)
    fixed_code_matches = fixed_code_pattern.search(input_string)
    
    fault_localisation_content = ""
    automatic_program_repair_content = ""
    fixed_code_content = ""
    
    if fault_localisation_matches:
        fault_localisation_content = fault_localisation_matches.group(1).strip()
    
    if automatic_program_repair_matches:
        automatic_program_repair_content = automatic_program_repair_matches.group(1).strip()
    
    if fixed_code_matches:
        fixed_code_content = fixed_code_matches.group(1).strip()
    
    return fault_localisation_content, automatic_program_repair_content, fixed_code_content

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


files_to_process = [
     "file_40", "file_113"
]

data_zs = []
data_os = []

df_input = pd.read_csv(input_csv, encoding = 'utf-8')

df_filtered = df_input[df_input.iloc[:, 0].isin(files_to_process)]

for index, col in df_filtered.iterrows():
    file_name = col[0]
    code_content = col[1]
    error_code = col[4]
    explanation = col[5]

    print(f"Processing {file_name}")

    # one-shot prompting
    if error_code == 'CE':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: There is a ' + explanation + ' in the code' + '\n\nCode:' + code_content
    elif error_code == 'TLE':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:' + code_content
    elif error_code == 'MLE':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:' + code_content
    elif error_code == 'RE':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:' + code_content
    elif error_code == 'WA':
        one_shot_prompt = base_prompt + '\n\n' + '\n\nCode Context: The output provides the ' + explanation + '\n\nCode:' + code_content

    # one-shot prompting
    chatgpt_response_os, input_tokens_os, output_tokens_os = prompt_chatgpt(one_shot_prompt)
    fault_localisation_output, reason_for_fix, fixed_code_content  = parse_response(chatgpt_response_os)

    print(f"chatgpt response: {chatgpt_response_os}")

    print(f"fault localisation: {fault_localisation_output}")
    print(f"reason for fix: {reason_for_fix}")

    print(f"fixed code: {fixed_code_content}")

    data_os.append([
        file_name, one_shot_prompt, chatgpt_response_os, input_tokens_os, output_tokens_os, fault_localisation_output, reason_for_fix, fixed_code_content
    ])

    with open(f"Responses/EvalGPTFix_GPT/Code/{file_name}.txt", 'w', encoding='utf-8') as file:
            file.write(fixed_code_content)

df_output_os = pd.DataFrame(data_os, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used', 'Fault Localisation', 'Reason for Fix', 'Fixed Code'
])

df_output_os.to_csv(output_csv2, index=False, encoding='utf-8')
