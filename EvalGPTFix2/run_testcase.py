import glob
import os
import subprocess

import pandas as pd
from os import listdir


def cleanFiles(name):
    java_files = glob.glob('{}.*'.format(name))

    for file_path in java_files:
        os.remove(file_path)

def run_all_test_case(code, task, memory):

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'AtCoderTestCasesOfficial/')
    path_to_test_case =  file_path + task
    input_files = os.listdir(path_to_test_case + "/in")
    output_files = os.listdir(path_to_test_case + "/out")
    f_java = open("Main.java", 'a', encoding='utf-8')
    f_java.write(code)
    f_java.close()
    compile_result = subprocess.run(['javac', '-J-Dfile.encoding=UTF8', 'Main.java'], capture_output=True, text=True,
                                    encoding='utf-8')

    assert len(input_files) == len(output_files)
    if compile_result.returncode != 0:
        print("Compilation Error!")
        cleanFiles("Main")
        return [{'res':'CE'}]
    if len(input_files) == 0:
        print("No testcase to run!")
        cleanFiles("Main")
        return {'NT': "0/0"}
    else:
        num_test_case = (int)(len(input_files))
        count = 0
        res=[]
        for input_file, output_file in zip(input_files, output_files):
            input_path = path_to_test_case + "/in/" + input_file
            output_path = path_to_test_case + "/out/" + output_file
            input = open(input_path, 'r').read()
            expect_output = open(output_path, 'r').read()
            # 运行Java代码并向标准输入流中传递数据
            process = subprocess.Popen(['java', '-Xmx{}m'.format(memory), 'Main'], stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            try:
                actual_output, errors = process.communicate(input=input.encode('utf-8'), timeout=10)
            except subprocess.TimeoutExpired:
                print("Time Limit Exceed Error!")
                # cleanFiles("Main")
                res.append({'res': 'TLE', 'input': input, 'expect': expect_output})
                # res.append({'res': 'TLE'})
                process.kill()
                continue
                # return {'res': 'TLE', 'input': input, 'expect': expect_output}
            if errors.decode('utf-8') != '':
                if 'Invalid maximum heap size' in errors.decode('utf-8'):
                    print('Memory Limit Exceed')
                    res.append({'res': 'MLE', 'input': input, 'expect': expect_output})
                    # res.append({'res':'MLE'})
                    process.kill()
                    continue
                    # return {'res': 'MLE', 'input': input, 'expect': expect_output}
                else:
                    print("Runtime Error!")
                    res.append({'res':'RE', 'input':input, 'expect': expect_output})
                    # res.append({'res':'RE'})
                    process.kill()
                    continue
                    # return {'res':'RE', 'input':input, 'expect': expect_output}
                # return {'RE': errors.decode('utf-8')}
            # if actual_output.decode(encoding='utf-8').strip() == expect_output.strip():
            #     count += 1
            # else:
            #     print("One testcase failed!")
            #     print(expect_output)
            #     print(actual_output.decode(encoding='utf-8'))
            if not actual_output.decode(encoding='utf-8').strip() == expect_output.strip():
                print('Wrong Answer!')
                res.append({'res':'WA', 'input': input, 'expect': expect_output,'actual':actual_output.decode(encoding='utf-8')})
                # res.append({'res':'WA'})
                print(f"Expected Output: " + expect_output)
                print(f"Actual Output: " + actual_output.decode(encoding='utf-8'))
                process.kill()
                continue
                # return {'res':'WA', 'input': input, 'expect': expect_output,'actual':actual_output.decode(encoding='utf-8')}

            res.append({'res':'AC'})
            process.kill()

        # print("All testcases passed!")
        cleanFiles("Main")
        for file_name in listdir('./'):
            if file_name.endswith('.class') or file_name.startswith('Main'):
                os.remove(file_name)

        # return {'res':'AC'}
        return res


def run_test_case(code, task, memory, file_name_actual):

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'AtCoderTestCasesOfficial/')
    path_to_test_case =  file_path + task
    input_files = os.listdir(path_to_test_case + "/in")
    output_files = os.listdir(path_to_test_case + "/out")
    f_java = open("Main.java", 'a', encoding='utf-8')
    f_java.write(code)
    f_java.close()
    compile_result = subprocess.run(['javac', '-J-Dfile.encoding=UTF8', 'Main.java'], capture_output=True, text=True,
                                    encoding='utf-8')
    
    response = []

    assert len(input_files) == len(output_files)
    if compile_result.returncode != 0:
        print("Compilation Error!")
        response.append("Compilation Error!")
        cleanFiles("Main")
        return {'res':'CE'}
    if len(input_files) == 0:
        print("No testcase to run!")
        response.append("No testcase to run!")
        cleanFiles("Main")
        return {'NT': "0/0"}
    else:
        num_test_case = (int)(len(input_files))
        count = 0
        res=[]
        for input_file, output_file in zip(input_files, output_files):
            input_path = path_to_test_case + "/in/" + input_file
            output_path = path_to_test_case + "/out/" + output_file
            input = open(input_path, 'r').read()
            expect_output = open(output_path, 'r').read()
            process = subprocess.Popen(['java', '-Xmx{}m'.format(memory), 'Main'], stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            try:
                actual_output, errors = process.communicate(input=input.encode('utf-8'), timeout=10)
            except subprocess.TimeoutExpired:
                print("Time Limit Exceed Error!")
                response.append("Time Limit Exceed Error!")
                # cleanFiles("Main")
                # res.append({'res': 'TLE', 'input': input, 'expect': expect_output})
                # res.append({'res': 'TLE'})
                process.kill()
                # continue
                return {'res': 'TLE', 'input': input, 'expect': expect_output}
            if errors.decode('utf-8') != '':
                if 'Invalid maximum heap size' in errors.decode('utf-8'):
                    print('Memory Limit Exceed')
                    response.append("Memory Limit Exceed")
                    # res.append({'res': 'MLE', 'input': input, 'expect': expect_output})
                    # res.append({'res':'MLE'})
                    process.kill()
                    # continue
                    return {'res': 'MLE', 'input': input, 'expect': expect_output}
                else:
                    print("Runtime Error!")
                    response.append("Runtime Error!")
                    # res.append({'res':'RE', 'input':input, 'expect': expect_output})
                    # res.append({'res':'RE'})
                    process.kill()
                    # continue
                    return {'res':'RE', 'input':input, 'expect': expect_output}
                # return {'RE': errors.decode('utf-8')}
            # if actual_output.decode(encoding='utf-8').strip() == expect_output.strip():
            #     count += 1
            # else:
            #     print("One testcase failed!")
            #     print(expect_output)
            #     print(actual_output.decode(encoding='utf-8'))
            # Split the actual and expected outputs into lines and strip each line
            actual_lines = actual_output.decode('utf-8').strip().splitlines()
            expect_lines = expect_output.strip().splitlines()

            # Compare the outputs line by line
            if actual_lines == expect_lines:
                print('Correct Answer!')
                response.append("Correct Answer!")
                res.append({'input': input, 'expect': expect_output, 'actual': actual_output.decode('utf-8')})
                # print(f"Expected Output: {expect_output}")
                # print(f"Actual Output: {actual_output.decode('utf-8')}")
            else:
                print('Wrong Answer!')
                response.append("Wrong Answer!")
                res.append({'input': input, 'expect': expect_output, 'actual': actual_output.decode('utf-8')})
                # print(f"Expected Output: {expect_output}")
                # print(f"Actual Output: {actual_output.decode('utf-8')}")
                
            process.kill()
            continue

            # res.append({'res':'AC'})
            process.kill()

        with open(f'{file_name_actual}_test_results.txt', 'w') as file:
            file.write(file_name_actual)
            file.write('\n')
            file.write('test results:')
            file.write(str(response))

        # print("All testcases passed!")
        cleanFiles("Main")
        for file_name in listdir('./'):
            if file_name.endswith('.class') or file_name.startswith('Main'):
                os.remove(file_name)

        return {'res':'AC'}
        # return res


if __name__ == '__main__':
    code = '''
import java.util.Scanner; // Import statement added for Scanner

public class Main {
    public static void main(String[] args) {
        int n, l, r, p, xr = 0;
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        l = scanner.nextInt();
        r = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            p = scanner.nextInt();
            xr ^= (p % (l + r)) / l;
        }
        System.out.println((xr > 0) ? "First" : "Second");
    }
}
    '''
    task = "abc297/G"
    test_res=run_test_case(code, task, 1024)
    print(test_res)
    for res in test_res:
         print(res)
    print(run_test_case(code, task, 1024))
