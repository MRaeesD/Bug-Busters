import os
import pandas as pd
import requests
from dotenv import load_dotenv
import google.generativeai as genai
import re

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

input_csv = './QuixBugs_Extracted/ExtractedJavaQuixBugs.csv'
output_csv1 = './Responses/QuixBugs_Gemini/zero_shot_Gemini_1.0_Pro_Java.csv'
output_csv2 = './Responses/QuixBugs_Gemini/one_shot_Gemini_1.0_Pro_Java.csv'

base_prompt = '''Please analyse the Java code snippet provided above. Identify the intention of the code and potential bugs in the code.
The response should contain up to three objects, ordered from the most probable to least probable code line to contain a bug.
\nYour response should be in the following template structure. Be mindful of indentation:
    ```
        {
        "Intention": <Brief description of the code's purpose>,

        "Fault Localisation": [
            {
            "Buggy Code Line": <Line number of buggy code. Do not use quotation marks>,
            "Code": <Actual buggy code>,
            "Reason": <Reason for the bug>
            },
            ...
        ]
        }
    ```
'''

def prompt_gemini(content):
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content(content)
    message_content = response.text.strip()
    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count
    return message_content, input_tokens, output_tokens

def parse_response(response):

    extracted_info = []
    
    bug_pattern = re.compile(r'\{\s*"Buggy Code Line":\s*(\d+),\s*"Code":\s*"([^"]+)",\s*"Reason":\s*"([^"]+)"\s*\}')
    
    intent = re.compile(r'\{\s*"Intention":\s*"([^"]+)"')

    bugs = bug_pattern.findall(response)
    
    extracted_intent = intent.findall(response)
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
    gemini_response_zs, input_tokens_zs, output_tokens_zs = prompt_gemini(zero_shot_prompt)
    bugs_zs, intent_zs = parse_response(gemini_response_zs)

    while len(bugs_zs) < 3:
        bugs_zs.append({"Buggy Code Line": "", "Code": "", "Reason": ""})
    
    data_zs.append([
        file_name, zero_shot_prompt, gemini_response_zs, input_tokens_zs, output_tokens_zs, intent_zs,
        bugs_zs[0]["Buggy Code Line"], bugs_zs[0]["Code"], bugs_zs[0]["Reason"],
        bugs_zs[1]["Buggy Code Line"], bugs_zs[1]["Code"], bugs_zs[1]["Reason"],
        bugs_zs[2]["Buggy Code Line"], bugs_zs[2]["Code"], bugs_zs[2]["Reason"]
    ])

    # one-shot prompting
    gemini_response_os, input_tokens_os, output_tokens_os = prompt_gemini(one_shot_prompt)
    bugs_os, intent_os = parse_response(gemini_response_os)

    while len(bugs_os) < 3:
        bugs_os.append({"Buggy Code Line": "", "Code": "", "Reason": ""})
    
    data_os.append([
        file_name, one_shot_prompt, gemini_response_os, input_tokens_os, output_tokens_os, intent_os,
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