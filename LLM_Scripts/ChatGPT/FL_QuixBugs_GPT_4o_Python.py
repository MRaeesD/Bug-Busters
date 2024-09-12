import os
import pandas as pd
import requests
from dotenv import load_dotenv
import re

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

input_csv = './QuixBugs_Extracted/ExtractedPythonQuixBugs.csv'
output_csv1 = './Responses/QuixBugs_GPT/zero_shot_ChatGPT_4o_Python.csv'
output_csv2 = './Responses/QuixBugs_GPT/one_shot_ChatGPT_4o_Python.csv'

base_prompt = '''Please analyse the Python code snippet provided above. Identify the intention of the code and potential bugs in the code.
The response should contain up to three objects, ordered from the most probable to least probable code line to contain a bug.
\nYour response should be in the following template structure:
    ```
        {
        "Intention": <Brief description of the code's purpose>,

        "Fault Localisation": [
            {
            "Buggy Code Line": <Line number of buggy code>,
            "Code": <Actual buggy code>,
            "Reason": <Reason for the bug>
            },
            ...
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

def parse_response(response):

    extracted_info = []
    
    bug_pattern = re.compile(r'\{\s*"Buggy Code Line":\s*(\d+),\s*"Code":\s*"([^"]+)",\s*"Reason":\s*"([^"]+)"\s*\}')
    
    intent = re.compile(r'\{\s*"Intention":\s*"([^"]+)"')

    bugs = bug_pattern.findall(response)
    
    extracted_intent = intent.findall(response)
    if not extracted_intent:
        extracted_intent = ['-']
        
    for bug in bugs:
    
        bug_code_line = int(bug[0])
        code = bug[1]
        reason = bug[2]
        
        extracted_info.append({
            "Buggy Code Line": bug_code_line,
            "Code": code,
            "Reason": reason
        })
    
    return extracted_info, extracted_intent[0]

data_zs = []
data_os = []

df_input = pd.read_csv(input_csv)

for index, col in df_input.iterrows():
    file_name = col[0]
    code_content = col[1]
    explanation = col[2]

    print("Processing file:" + file_name + "\n")

    zero_shot_prompt = 'Code:' + code_content + '\n' + base_prompt
    one_shot_prompt = 'Code:' + code_content + '\nThe code is expected to function as follows:' + explanation + '\n\n' + base_prompt 

    # zero-shot prompting
    chatgpt_response_zs, input_tokens_zs, output_tokens_zs = prompt_chatgpt(zero_shot_prompt)
    bugs_zs, intent_zs = parse_response(chatgpt_response_zs)

    while len(bugs_zs) < 3:
        bugs_zs.append({"Buggy Code Line": "", "Code": "", "Reason": ""})
    
    data_zs.append([
        file_name, zero_shot_prompt, chatgpt_response_zs, input_tokens_zs, output_tokens_zs, intent_zs,
        bugs_zs[0]["Buggy Code Line"], bugs_zs[0]["Code"], bugs_zs[0]["Reason"],
        bugs_zs[1]["Buggy Code Line"], bugs_zs[1]["Code"], bugs_zs[1]["Reason"],
        bugs_zs[2]["Buggy Code Line"], bugs_zs[2]["Code"], bugs_zs[2]["Reason"]
    ])

    # one-shot prompting
    chatgpt_response_os, input_tokens_os, output_tokens_os = prompt_chatgpt(one_shot_prompt)
    bugs_os, intent_os = parse_response(chatgpt_response_os)

    while len(bugs_os) < 3:
        bugs_os.append({"Buggy Code Line": "", "Code": "", "Reason": ""})
    
    data_os.append([
        file_name, one_shot_prompt, chatgpt_response_os, input_tokens_os, output_tokens_os, intent_os,
        bugs_os[0]["Buggy Code Line"], bugs_os[0]["Code"], bugs_os[0]["Reason"],
        bugs_os[1]["Buggy Code Line"], bugs_os[1]["Code"], bugs_os[1]["Reason"],
        bugs_os[2]["Buggy Code Line"], bugs_os[2]["Code"], bugs_os[2]["Reason"]
    ])

df_output_zs = pd.DataFrame(data_zs, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used', "Code Intent",
    'Buggy Code Line 1', 'Code 1', 'Reason 1',
    'Buggy Code Line 2', 'Code 2', 'Reason 2',
    'Buggy Code Line 3', 'Code 3', 'Reason 3'
])
df_output_os = pd.DataFrame(data_os, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used',"Code Intent",
    'Buggy Code Line 1', 'Code 1', 'Reason 1',
    'Buggy Code Line 2', 'Code 2', 'Reason 2',
    'Buggy Code Line 3', 'Code 3', 'Reason 3'
])

df_output_zs.to_csv(output_csv1, index=False)
df_output_os.to_csv(output_csv2, index=False)