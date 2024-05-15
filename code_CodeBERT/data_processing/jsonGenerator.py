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

#Java file path
file_pathJv = "/home/siddharthsa/BugDetection/newBuggyFixedDataset1/SWAP_BOOLEAN_LITERAL/1"

#JSONL file path
file_pathJs = "/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/data.jsonl"

code_l = code_list(file_pathJv)

lbl = 1
#buggyMethod
#fixedMethod
#13
print(len(code_l))
labelType = 13
new_data = [{"fixedMethod": code, "labelBuggy": lbl, "labelType":labelType} for code in code_l]

# Append new data to the JSONL file
with open(file_pathJs, "a") as jsonl_file:
    for item in new_data:
        jsonl_file.write(json.dumps(item) + '\n')

print(f"New data has been appended to {file_pathJs}")