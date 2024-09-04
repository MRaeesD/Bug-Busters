import os
import pandas as pd

csv_file = './Datasets/EvalGPTFix/data/latest_contests_with_bug_location_new.csv'
df = pd.read_csv(csv_file, usecols=[3])
output_folder = './EvalGPTFix_Extracted/java_programs'

for i, element in enumerate(df.iloc[:, 0]):
    if i< 10:
        file_name = os.path.join(output_folder, f'file_0{i}.java')
        with open(file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(str(element))
    else:
        file_name = os.path.join(output_folder, f'file_{i}.java')
        with open(file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(str(element))

print("Files created successfully.")    