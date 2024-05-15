import os
import json
import string
#import pandas as pd


#reading all the files available in the given folder
def list_files_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    return files


# Function to remove comments from Java code
def remove_comments(code):
    lines = code.split('\n')
    clean_lines = []
    in_comment = False

    for line in lines:
        if not in_comment:
            clean_line = line.split("//")[0]  # Remove single-line comments
            if "/*" in clean_line:
                in_comment = True
                clean_line = clean_line.split("/*")[0]  # Remove starting multi-line comment
        else:
            if "*/" in line:
                in_comment = False
                clean_line = line.split("*/")[1]  # Remove ending multi-line comment
            else:
                clean_line = ""
        clean_lines.append(clean_line)
    
    return '\n'.join(clean_lines)

#finding buggy and fixed pair
def find_fixed_version(buggy_method, code_list_2):
    buggy_first_line = buggy_method.split("\n", 1)[0].strip()
    buggy_num_lines = buggy_method.count('\n') + 1  # Counting lines in buggy method
    for fixed_method in code_list_2:
        fixed_first_line = fixed_method.split("\n", 1)[0].strip()
        fixed_num_lines = fixed_method.count('\n') + 1  # Counting lines in fixed method
        if buggy_first_line == fixed_first_line and buggy_num_lines == fixed_num_lines:
            return fixed_method
    return None


#Reading java code from all the java files from a given folder
def code_list(folder_path):
    code = []
    file0 = list_files_in_folder(folder_path)

    for file in file0:
        file_pathJava = folder_path +"/" +file
        with open(file_pathJava, "r") as jVfile:
            jcode = jVfile.read()
        jcode = remove_comments(jcode) # Remove comments from Java code
        code.append(jcode)
    return code

#generate jsonl file
def generate_jsonl(code_list_1, code_list_2, file_path):
    new_data_1 = []
    new_data_2 = []
    with open(file_pathJs, "a") as jsonl_file:
        for buggy_method in code_list_1:
            fixed_method = find_fixed_version(buggy_method, code_list_2)
            if fixed_method:
                buggy_json = {"buggyMethod": buggy_method, "labelBuggy": 0, "labelType": 1}
                fixed_json = {"fixedMethod": fixed_method, "labelBuggy": 1, "labelType": 1}
                jsonl_file.write(json.dumps(buggy_json) + '\n')
                jsonl_file.write(json.dumps(fixed_json) + '\n')

#Java file path
file_path0 = "/home/siddharthsa/BugDetection/newBuggyFixedDataset1/SWAP_BOOLEAN_LITERAL/0"

#Java file path
file_path1 = "/home/siddharthsa/BugDetection/newBuggyFixedDataset1/SWAP_BOOLEAN_LITERAL/1"

#JSONL file path
file_pathJs = "/home/siddharthsa/BugDetection/newBuggyFixedDataset1/jsonlFiles/13.jsonl"

code_list_1 = code_list(file_path0)
code_list_1_unique = list(set(code_list_1))

code_list_2 = code_list(file_path1)
code_list_2_unique = list(set(code_list_2))


print(len(code_list_1_unique))
print(len(code_list_2_unique))

generate_jsonl(code_list_1_unique, code_list_2_unique, file_pathJs)

