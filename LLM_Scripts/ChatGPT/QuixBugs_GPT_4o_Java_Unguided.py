import os
import pandas as pd
import requests
from dotenv import load_dotenv
import re

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

input_csv_1 = './QuixBugs_Extracted/ExtractedJavaQuixBugs-APR.csv'
output_csv_2 = './Responses/QuixBugs_GPT/Unguided/ChatGPT_4o_Java.csv'

base_prompt = base_prompt = '''Debug the following Java code snippet. Localise the bug(s) and provide a fix for the bug and a reason for the fix. 
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
            "Fixed Code": <Fully fixed code, wrapped in a Python code block: ```java```. Do not use \n or \t>,
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

data_zs = []
data_os = []

df_input1 = pd.read_csv(input_csv_1)

for index, col in df_input1.iterrows():
    file_name = col[0]
    code_content = col[1]
    explanation = col[2]
    correction = col[4]

    print(f"Processing file: {file_name} \n")

    one_shot_prompt = base_prompt + '\n Code: ' + code_content + '\n Code Context: ' + explanation 

    # one-shot prompting
    chatgpt_response_os, input_tokens_os, output_tokens_os = prompt_chatgpt(one_shot_prompt)
    fault_localisation_output, reason_for_fix, fixed_code  = parse_response(chatgpt_response_os)

    print(f"chatgpt response: {chatgpt_response_os}")

    print(f"fixed code: {fixed_code}")

    data_os.append([
        file_name, one_shot_prompt, chatgpt_response_os, input_tokens_os, output_tokens_os, fault_localisation_output, reason_for_fix, fixed_code
    ])

    with open(f"Responses/QuixBugs_GPT/Unguided/Code/Java/{file_name}", 'w') as file:
            file.write(fixed_code)

df_output_os = pd.DataFrame(data_os, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used', 'Fault Localisation', 'Reason for Fix', 'Fixed Code'
])

df_output_os.to_csv(output_csv_2, index=False)
