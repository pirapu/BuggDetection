import json

# Read the contents of the JSONL file
with open('/home/siddharthsa/BugDetection/newBuggyFixedDataset1/jsonlFiles/2.jsonl', 'r') as file:
    lines = file.readlines()

# Modify the lines with labelType 1 to labelType 2
modified_lines = []
for line in lines:
    data = json.loads(line)
    if data.get("labelType") == "1":
        data["labelType"] = "2"
    modified_lines.append(json.dumps(data))

# Write the modified lines back to the file
with open('/home/siddharthsa/BugDetection/newBuggyFixedDataset1/modifiedJsonl/2.jsonl', 'w') as file:
    file.write('\n'.join(modified_lines))
