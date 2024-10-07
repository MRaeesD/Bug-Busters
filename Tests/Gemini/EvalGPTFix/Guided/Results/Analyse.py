import os
import csv

folder_path = os.path.dirname(__file__)

keywords = ["Compilation Error!", "No testcase to run!", "Time Limit Exceed Error!", "Memory Limit Exceed", "Runtime Error!", "Wrong Answer!"]

csv_file_path = os.path.join(folder_path, 'analysis_results_Gemini_Guided.csv')

def check_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        for keyword in keywords:
            if keyword in content:
                return False
    return True

results = []
true_count = 0

for n in range(151):
    filename = f'file_{n}_test_results.txt'
    file_path = os.path.join(folder_path, filename)
    if os.path.exists(file_path):
        result = check_file(file_path)
        results.append([filename, result])
        if result:
            true_count += 1

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Filename', 'IsTrue'])
    csvwriter.writerows(results)

print(f"Analysis complete. Results saved to {csv_file_path}")
print(f"Number of files that are true: {true_count}")