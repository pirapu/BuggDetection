import json
import string
import pandas as pd
import numpy as np
import os

data = pd.read_json("/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/dataset.jsonl", lines=True)
print("Total samples in test set: ", len(data))

def read_jsonl_subset(input_file, start_line, end_line):
    output_data = []
    with open(input_file, 'r') as f:
        for i, line in enumerate(f):
            if start_line <= i + 1 <= end_line:
                output_data.append(line.strip())
            elif i + 1 > end_line:
                break
    return output_data

def write_jsonl(output_file, data):
    with open(output_file, 'w') as f:
        for line in data:
            f.write(line + '\n')

input_file = "/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/dataset.jsonl"
output_file = "/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/test.jsonl"
start_line = 25963  # Start line index (1-based)
end_line = 27300    # End line index (1-based)

subset_data = read_jsonl_subset(input_file, start_line, end_line)
write_jsonl(output_file, subset_data)

