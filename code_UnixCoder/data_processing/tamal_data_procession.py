import os
import string
import json

root_directory = '/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/Java250_processed_data_for_pdg'

def extract_number(directory):
    # Split the directory path by '/'
    parts = directory.split('/')
    # Find the part containing the number
    for part in parts:
        if part.startswith('p'):
            # Extract the number after 'p'
            return int(part[1:])
    # If no number is found, return 0
    return 0

def list_files(root_directory):
    all_files = []
    all_dirs = []
    for root, dirs, files in os.walk(root_directory):
        for dir in dirs:
            all_dirs.append(dir)
        # Sort directories based on the number extracted from the directory path
        dirs.sort(key=extract_number)
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files, all_dirs

java_files, java_dir = list_files(root_directory)
#print(sub_dirs[0])
#print(java_files[0])
#print(len(java_files))

with open("/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/java_files.txt", "w") as f:
    for fle in java_files:
        f.write("%s\n" % fle)   

print(len(java_files))

type = "p00001"
i = 0
# new_data = []
# for file_path in java_files:
#     new_type = file_path.split("/")[7]
#     filename = file_path.split("/")[8].split(".")[0]
#     #print(filename)
#     with open(file_path, "r") as jVfile:
#             jcode = jVfile.read()
#     if type == new_type:
#         json_str = json.dumps({"code": jcode, "label": i, "fileName": filename})
#         new_data.append(json_str)
#         #print(i)
#     else:
#         type = new_type
#         i = i+1
#         json_str = json.dumps({"code": jcode, "label": i, "fileName": filename})
#         new_data.append(json_str)

# with open("/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/tamal_data.jsonl", "w") as f:
#     for item in new_data:
#         f.write("%s\n" % item)

# path = "/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/Java250_processed_data_for_pdg/p00001/s742637637.java"
# new_types = path.split("/")[7]
# print(new_types)

#print(len(new_data))