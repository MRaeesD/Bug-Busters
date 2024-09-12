import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

input_csv = './EvalGPTFix_Extracted/ExtractedEvalGPTFix_test.csv'
output_csv1 = './Responses/Gemini_EvalGPTFix/TEST_zero_shot_Gemini1.5_EvalGPTFix.csv'
output_csv2 = './Responses/Gemini_EvalGPTFix/TEST_one_shot_Gemini1.5_EvalGPTFix.csv'

# prompt_test = '''Please identify the bug in the following Java code snippet.\n
#                 Indicate:\n
#                 Buggy code lines: The specific lines of code that are incorrect.\n
#                 Omitted lines: If there are missing lines of code that would be necessary 
#                 for the code to function correctly, please indicate where they should be inserted.\n

#                 The code can either have buggy code lines, omitted lines, or both. 

#                 Format your response like this: \n 

#                 Buggy Code Lines: <Buggy Code Lines 1> <Buggy Code Lines 2> or <N/A> (if there are no buggy lines) ...\n
#                 (skip a line after the buggy code lines)\n

#                 Reason: <Reason for bug without a fix>\n
#                 (skip a line after the reason)\n
                
#                 Omitted Lines: <True> or <False> or <N/A> (if there are no omitted lines) ...\n
#                 (skip a line after the omitted lines)\n 

#                 Location: <Indicate where the omitted lines should be inserted (e.g., "after this line of code <insert code>")>
#                 '''

prompt_test = '''Please analyse the Python code snippet provided above and identify the potential bugs in the code. 

                \nYour response should be in JSON format with the following template structure:
```json
                {
                "faultLocalisation": [
                    {
                    "Faulty Code Line": (indicating the line number of the suspicious code),
                    "Code": (displaying the actual code),
                    "Explanation": (step by step reasoning on why this location is considered potentially faulty)
                    },
                    ...
                ]
                }
                ```

Note: The JSON should contain up to three objects and should be listed in descending of highest suspicion.
'''

def prompt_gemini(content):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(content)
    return response.text

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
    gemini_response_zs = prompt_gemini(zero_shot_prompt)
    print(gemini_response_zs)
