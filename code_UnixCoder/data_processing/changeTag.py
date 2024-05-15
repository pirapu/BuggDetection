import json

input_file = "/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/train.jsonl"
output_file = "/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/train1.jsonl"

with open(input_file, "r") as f:
    lines = f.readlines()

modified_lines = []
for line in lines:
    data = json.loads(line)
    if "buggyMethod" in data:
        data["code"] = data.pop("buggyMethod")
    elif "fixedMethod" in data:
         data["code"] = data.pop("fixedMethod")
    # Reorder the keys
    ordered_data = {"code": data["code"], "labelBuggy": data.get("labelBuggy"), "labelType": data.get("labelType")}
    modified_lines.append(json.dumps(ordered_data))

with open(output_file, "w") as f:
    f.write("\n".join(modified_lines))

print(f"Successfully converted 'buggyMethod' tags to 'code' and saved to {output_file}.")
