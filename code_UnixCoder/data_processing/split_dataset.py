import json
import random
from collections import defaultdict
import pandas as pd


def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def split_data(data, train_ratio=0.7, val_ratio=0.20, test_ratio=0.10):
    class_data = defaultdict(list)

    for entry in data:
        class_data[entry['labelBuggy']].append(entry)
    
    train_data = []
    val_data = []
    test_data = []

    for class_name, class_entries in class_data.items():
        random.shuffle(class_entries)
        total_entries = len(class_entries)
        
        train_size = int(total_entries * train_ratio)
        val_size = int(total_entries * val_ratio)
        test_size = total_entries - train_size - val_size
        
        train_data.extend(class_entries[:train_size])
        val_data.extend(class_entries[train_size:train_size+val_size])
        test_data.extend(class_entries[train_size+val_size:])


    return train_data, val_data, test_data

# Example usage:
data = read_jsonl("/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/dataset1.jsonl")

train_data, val_data, test_data = split_data(data)

# print("Train set size:", len(train_data))
# print("Validation set size:", len(val_data))
# print("Test set size:", len(test_data))

# print(train_data[0])

# # list = pd.read_jsonl(train_data)
# list = pd.DataFrame.from_dict(train_data)['labelBuggy']

# print(len(list))

# count_zero, count_one = 0,0 

# for l in list:
#     if l == 0:
#         count_zero = count_zero + 1
#         # zero.append(l)
#     elif l == 1:
#         count_one = count_one + 1

# print(f"Count for Buggy: ", count_zero, "|||| Count for Non-Buggy: ", count_one)
random.shuffle(val_data)
file_pathN = "/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/valid.jsonl"
# Append new data to the JSONL file
with open(file_pathN, "a") as jsonl_file:
    for item in val_data:
        jsonl_file.write(json.dumps(item) + '\n')




