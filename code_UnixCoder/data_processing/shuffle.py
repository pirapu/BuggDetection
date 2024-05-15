import json
import random

file_path = "/home/siddharthsa/BugDetection/shuffled_data.jsonl"
def write_jsonl(output_file, data):
    with open(output_file, 'w') as f:
        for line in data:
            f.write(line + '\n')

with open("/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/dataset.jsonl") as f:
     data = json.load(f)

random.shuffle(data)

write_jsonl(file_path, data)