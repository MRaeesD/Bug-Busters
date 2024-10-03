import os
import pandas as pd
import requests
from dotenv import load_dotenv
import re
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

input_csv_1 = './QuixBugs_Extracted/ExtractedPythonQuixBugs-APR.csv'
output_csv_2 = './Responses/QuixBugs_gemini/FL_APR_Combined/FL_APR_Combined_Gemini_1.5_Pro_Python.csv'

base_prompt = '''Debug the following Python code snippet. Localise the bug(s) and provide a fix for the bug and a reason for the fix. 
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
            "Fixed Code": <Fully fixed code, wrapped in a Python code block: ``` Python ```. Do not use \n or \t. Comment the location of the bug>,
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
    fixed_code_pattern = re.compile(r'"Fixed Code":\s*```python(.*?)```', re.DOTALL)
    
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

data_os = []

df_input1 = pd.read_csv(input_csv_1)

for index, col in df_input1.iterrows():
    file_name = col[0]
    code_content = col[1]
    explanation = col[2]

    print(f"Processing file: {file_name} \n")

    one_shot_prompt = base_prompt + '\n Code: ' + code_content + '\n Code Context: ' + explanation

    # one-shot prompting
    gemini_response_os, input_tokens_os, output_tokens_os = prompt_gemini(one_shot_prompt)
    fault_localisation_output, automatic_program_repair_output, fixed_code_content  = parse_response(gemini_response_os)

    print(f"fault localisation: {fault_localisation_output}")
    print(f"automatic program repair: {automatic_program_repair_output}")
    print(f"fixed code: {fixed_code_content}")
    print(f"gemini response: {gemini_response_os}")
    
    with open(f"./Responses/QuixBugs_Gemini/FL_APR_Combined/Code/1.5_pro_python/1.5_pro_python_{file_name}", 'w') as file:
        file.write(fixed_code_content+"\n")

    data_os.append([
        file_name, one_shot_prompt, gemini_response_os, input_tokens_os, output_tokens_os, fault_localisation_output, automatic_program_repair_output, fixed_code_content
    ])

df_output_os = pd.DataFrame(data_os, columns=[
    'File Name', 'Prompt', 'Full Response', 'Input Tokens Used', 'Output Tokens Used',"Fault Localisation", "Automatic Program Repair", "fixed code"
])

df_output_os.to_csv(output_csv_2, index=False)

