import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

input_csv = './EvalGPTFix_Extracted/ExtractedEvalGPTFix.csv'
output_csv1 = './Responses/Gemini_EvalGPTFix/zero_shot_Gemini1.0_EvalGPTFix.csv'
output_csv2 = './Responses/Gemini_EvalGPTFix/one_shot_Gemini1.0_EvalGPTFix.csv'

prompt_test = '''Please identify the bug in the following java code snippet. 
                \nOnly indicate the location of the bug and the reason it is a bug (without providing a fix) in the format: 
                \nLine Number: <Line number> (skip a line after the line number)
                \nLine of Code: <Line of code with the bug> (skip a line after the code line)
                \nReason: <Reason without a fix>'''

def prompt_gemini(content):
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content(content)
    inputTokens = response.usage_metadata.prompt_token_count
    outputTokens = response.usage_metadata.candidates_token_count
    totalTokens = response.usage_metadata.total_token_count
    return response.text.strip(), inputTokens, outputTokens, totalTokens

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
    error_code = col[2]
    explanation = col[3]
    print(file_name)
    
    # zero-shot prompting
    zero_shot_prompt = prompt_test + '\n\n' + code_content
    gemini_response_zs, inputTokens_zs, outputTokens_zs, totalTokens_zs = prompt_gemini(zero_shot_prompt)
    bug_line_number_zs, buggy_line_zs, reason_for_bug_zs = parse_response(gemini_response_zs)
    data_zs.append([file_name, zero_shot_prompt, gemini_response_zs, bug_line_number_zs, buggy_line_zs, reason_for_bug_zs, inputTokens_zs, outputTokens_zs, totalTokens_zs])
    
    # one-shot prompting
    if error_code == 'CE':
        one_shot_prompt = prompt_test + '\n\n' + '\n\nCode Context: There is a ' + explanation + ' in the code' + '\n\nCode:' + code_content
    elif error_code == 'TLE':
        one_shot_prompt = prompt_test + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:' + code_content
    elif error_code == 'MLE':
        one_shot_prompt = prompt_test + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:' + code_content
    elif error_code == 'RE':
        one_shot_prompt = prompt_test + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:' + code_content
    elif error_code == 'WA':
        one_shot_prompt = prompt_test + '\n\n' + '\n\nCode Context: The output provides the ' + explanation + '\n\nCode:' + code_content
    else:
        one_shot_prompt = zero_shot_prompt
        
    gemini_response_os, inputTokens_os, outputTokens_os, totalTokens_os = prompt_gemini(one_shot_prompt)
    bug_line_number_os, buggy_line_os, reason_for_bug_os = parse_response(gemini_response_os)
    data_os.append([file_name, one_shot_prompt, gemini_response_os, bug_line_number_os, buggy_line_os, reason_for_bug_os, inputTokens_os, outputTokens_os, totalTokens_os])

df_output_zs = pd.DataFrame(data_zs, columns=['File Name', 'Prompt', 'Full Response', 'Bug Line Number', 'Code Line with Bug', 'Reason for Bug', 'Input Tokens', 'Output Tokens', 'Total Tokens'])
df_output_os = pd.DataFrame(data_os, columns=['File Name', 'Prompt', 'Full Response', 'Bug Line Number','Code Line with Bug', 'Reason for Bug', 'Input Tokens', 'Output Tokens', 'Total Tokens'])

df_output_zs.to_csv(output_csv1, index=False)
df_output_os.to_csv(output_csv2, index=False)

