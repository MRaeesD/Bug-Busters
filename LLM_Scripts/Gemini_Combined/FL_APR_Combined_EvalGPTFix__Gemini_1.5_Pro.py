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
# output_csv2 = './Responses/EvalGPTFix_Gemini/Gemini_1.5_Pro_EvalGPTFix.csv'
output_csv2 = './Responses/EvalGPTFix_Gemini/3EXTRA_Gemini_1.5_Pro_EvalGPTFix.csv'


base_prompt = '''Debug the following Java code snippet. Localise the bug(s), provide a fix for the bug(s) and a reason for the fix. 
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
            "Fixed Code": <Fully fixed code, wrapped in a Java code block. Preserve proper indentation.>,
            "Reason for Fix": <Reason for the fix>
            },
        ]   
        }
    ```
'''

def prompt_gemini(content):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(content)
    message_content = response.text.strip()
    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count
    return message_content, input_tokens, output_tokens

def parse_response(input_string):
    # Define regex patterns to extract the fault localisation and automatic program repair sections
    fault_localisation_pattern = re.compile(r'"Fault Localisation": \[(.*?)\],\s*"Automatic Program Repair"', re.DOTALL)
    automatic_program_repair_pattern = re.compile(r'"Automatic Program Repair": \[(.*?)\]\s*}', re.DOTALL)
    fixed_code_pattern = re.compile(r'"Fixed Code":\s*```java(.*?)```', re.DOTALL)
    
    # Search for the patterns in the input string
    fault_localisation_matches = fault_localisation_pattern.search(input_string)
    automatic_program_repair_matches = automatic_program_repair_pattern.search(input_string)
    fixed_code_matches = fixed_code_pattern.search(input_string)
    
    # Initialize variables to store the extracted content
    fault_localisation_content = ""
    automatic_program_repair_content = ""
    fixed_code_content = ""
    
    # Extract the content if matches are found
    if fault_localisation_matches:
        fault_localisation_content = fault_localisation_matches.group(1).strip()
    
    if automatic_program_repair_matches:
        automatic_program_repair_content = automatic_program_repair_matches.group(1).strip()
    
    if fixed_code_matches:
        fixed_code_content = fixed_code_matches.group(1).strip()
    
    return fault_localisation_content, automatic_program_repair_content, fixed_code_content

# files_to_process = [
#     "file_0", "file_1", "file_2", "file_3", "file_4", "file_5", "file_6", "file_7", "file_8", "file_9", "file_10",
#     "file_11", "file_12", "file_13", "file_14", "file_15", "file_16", "file_17", "file_18", "file_21",
#     "file_23", "file_25", "file_26", "file_27", "file_28", "file_30", "file_31", "file_35", "file_36",
#     "file_38", "file_39", "file_40"
# ]

files_to_process = [
    "file_23"
]

data_zs = []
data_os = []

df_input = pd.read_csv(input_csv, encoding = 'utf-8')

df_filtered = df_input[df_input.iloc[:, 0].isin(files_to_process)]

for index, col in df_filtered.iterrows():
# for index, col in df_input.iterrows():

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
    gemini_response_os, input_tokens_os, output_tokens_os = prompt_gemini(one_shot_prompt)
    fault_localisation_output, automatic_program_repair_output, fixed_code_content  = parse_response(gemini_response_os)

    print(f"fault localisation: {fault_localisation_output}")
    print(f"automatic program repair: {automatic_program_repair_output}")
    print(f"fixed code: {fixed_code_content}")
    print(f"gemini response: {gemini_response_os}")
    
    data_os.append([
        file_name, one_shot_prompt, gemini_response_os, input_tokens_os, output_tokens_os, fault_localisation_output, automatic_program_repair_output, fixed_code_content
    ])

    with open(f"Responses/EvalGPTFix_Gemini/Code/{file_name}.txt", 'w', encoding = 'utf-8') as file:
        file.write(fixed_code_content)

df_output_os = pd.DataFrame(data_os, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used',"Fault Localisation", "Automatic Program Repair", "fixed code"
])

df_output_os.to_csv(output_csv2, index=False, encoding = 'utf-8')