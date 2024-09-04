import os
import pandas as pd

csv_file = './Datasets/EvalGPTFix/data/latest_contests_with_bug_location_new.csv'
df = pd.read_csv(csv_file, usecols=[3, 4, 5])  # Include column 6 in the list of columns to be read

# Add a new column 'file_name' to df
new_df = pd.DataFrame({'file_name': [f'file_{i}' for i in range(len(df))]})
new_df = pd.concat([new_df, df], axis=1)
new_df.rename(columns={'error_type': 'error_code'}, inplace=True)

new_df['type_of_error'] = new_df['error_code'].apply(lambda x: 'Compilation Error' if x == 'CE' else x)
new_df['type_of_error'] = new_df['type_of_error'].apply(lambda x: 'Time Limit Exceeded' if x == 'TLE' else x)
new_df['type_of_error'] = new_df['type_of_error'].apply(lambda x: 'Memory Limit Exceeded' if x == 'MLE' else x)
new_df['type_of_error'] = new_df['type_of_error'].apply(lambda x: 'Runtime Error' if x == 'RE' else x)
new_df['type_of_error'] = new_df['type_of_error'].apply(lambda x: 'Wrong Answer' if x == 'WA' else x)

output_folder = './EvalGPTFix_Extracted'  # Replace with the desired output folder path
new_df.to_csv(os.path.join(output_folder, 'ExtractedEvalGPTFix.csv'), index=False)

print("CSV file created successfully.")