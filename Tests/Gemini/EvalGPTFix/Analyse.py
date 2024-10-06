import os
import csv

# Define the folder path
folder_path = os.path.dirname(__file__)

# Define the keywords to search for
keywords = ["Compilation Error!", "No testcase to run!", "Time Limit Exceed Error!", "Memory Limit Exceed", "Runtime Error!", "Wrong Answer!"]

# Prepare the CSV file
csv_file_path = os.path.join(folder_path, 'analysis_results.csv')

# Function to check if a file contains any of the keywords
def check_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        for keyword in keywords:
            if keyword in content:
                return False
    return True

# List to store the results
results = []
true_count = 0  # Counter for true results

# Iterate through all text files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        result = check_file(file_path)
        results.append([filename, result])
        if result:
            true_count += 1

# Write the results to the CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Filename', 'IsTrue'])
    csvwriter.writerows(results)

print(f"Analysis complete. Results saved to {csv_file_path}")
print(f"Number of files that are true: {true_count}")