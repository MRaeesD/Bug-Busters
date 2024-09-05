import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

input_csv = './QuixBugs_Extracted/ExtractedJavaQuixBugs.csv'
output_csv1 = './Responses/QuixBugs/zero_shot_ChatGPT_3.5_Java.csv'
output_csv2 = './Responses/QuixBugs/one_shot_ChatGPT_3.5_Java.csv'

prompt_test = '''Please identify the bug in the following Java code snippet. 
                \nOnly indicate the location of the bug and the reason it is a bug (without providing a fix) in the format: 
                \nLine Number: <Line number> (skip a line after the line number)
                \nLine of Code: <Line of code with the bug> (skip a line after the code line)
                \nReason: <Reason without a fix>'''

def prompt_chatgpt(content):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": "gpt-3.5-turbo", 
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

    print(f"Processing file: {file_name}")
    
    zero_shot_prompt = prompt_test + '\n\nCode:\n' + code_content
    one_shot_prompt = prompt_test + '\n\nCode Context:\n' + explanation + '\n\nCode:\n' + code_content

    # zero-shot prompting
    chatgpt_response_zs, input_tokens_zs, output_tokens_zs = prompt_chatgpt(zero_shot_prompt)
    bug_line_number_zs, buggy_line_zs, reason_for_bug_zs = parse_response(chatgpt_response_zs)
    data_zs.append([file_name, zero_shot_prompt, chatgpt_response_zs, input_tokens_zs, output_tokens_zs , bug_line_number_zs, buggy_line_zs, reason_for_bug_zs])
    
    # one-shot prompting
    chatgpt_response_os, input_tokens_os, output_tokens_os = prompt_chatgpt(one_shot_prompt)
    bug_line_number_os, buggy_line_os, reason_for_bug_os = parse_response(chatgpt_response_os)
    data_os.append([file_name, one_shot_prompt,chatgpt_response_os, input_tokens_os, output_tokens_os, bug_line_number_os, buggy_line_os, reason_for_bug_os])

df_output_zs = pd.DataFrame(data_zs, columns=['File Name', 'Prompt','Full Response','Input Tokens Used', 'Output Tokens Used' ,'Bug Line Number', 'Code Line with Bug', 'Reason for Bug'])
df_output_os = pd.DataFrame(data_os, columns=['File Name', 'Prompt','Full Response', 'Input Tokens Used', 'Output Tokens Used','Bug Line Number','Code Line with Bug', 'Reason for Bug'])

df_output_zs.to_csv(output_csv1, index=False)
df_output_os.to_csv(output_csv2, index=False)