from run_testcase import run_all_test_case
from run_testcase import run_test_case
from os import listdir
import os
import pandas as pd

script_dir = os.path.dirname(__file__)

input_csv = os.path.join(script_dir, 'ExtractedEvalGPTFix2.csv')

files_to_process = [
    "file_0", "file_1", "file_2"
]

# files_to_process = [
#     "file_4"
# ]

df_input = pd.read_csv(input_csv)

df_filtered = df_input[df_input.iloc[:, 0].isin(files_to_process)]

for index, col in df_filtered.iterrows():
    file_name = col[0]
    problem_id = str(col[7])

    file_path = os.path.join(script_dir, f"{file_name}.txt")
    print(file_path)
    print(problem_id)

    print(f"Processing {file_name}")
    code = ''
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
            # print(code)
        # test_res = run_all_test_case(code, problem_id, 2048)
        test_res = run_test_case(code, problem_id, 2048, file_name)

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")