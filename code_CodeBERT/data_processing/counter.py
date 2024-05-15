import json
import string
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_json("/home/siddharthsa/BugDetection/CodeBERT-classification/dataset/dataset1.jsonl", lines=True)
print("Total samples in test set: ", len(data))

total_dataset_size = len(data)
train_split_ratio = 0.7
test_split_ratio = 0.1
val_split_ratio = (1 - train_split_ratio) - test_split_ratio
print(train_split_ratio, val_split_ratio, test_split_ratio)

list = data['labelBuggy']

print(len(list))

# zero = []
count_zero, count_one = 0,0 

for l in list:
    if l == 0:
        count_zero = count_zero + 1
        # zero.append(l)
    elif l == 1:
        count_one = count_one + 1

print(f"Count for Buggy: ", count_zero, "|||| Count for Non-Buggy: ", count_one)

data_x = data['code']
data_y = data['labelBuggy']
print(data_y[:5])

# print(len(data_y))

y_buggy_count = 0
for i in data_y:
    if i == 0:
        y_buggy_count = y_buggy_count + 1
    elif i == 1:
        y_buggy_count = y_buggy_count - 1

print("Buggg", y_buggy_count)


data_x_train, data_x_test, data_y_train, data_y_test = train_test_split(data_x, data_y, stratify=data_y, test_size=9013, random_state=5, shuffle=True)

print(len(data_x_train), len(data_x_test))
print(len(data_y_train), len(data_y_test))

count_zero, count_one = 0,0 
print(type(data_y_train))
print("Showing Training")
print((data_y_train == 0).sum())
print((data_y_train == 1).sum())
print("Down showing")

# print(data_y_train[:5])

for l in data_y_train:
    if l == 0:
        count_zero = count_zero + 1
        # zero.append(l)
    elif l == 1:
        count_one = count_one + 1
print(count_zero, count_one)

# print(y_test)

code_train,  code_test, label_train, label_test = train_test_split(data_x_test, data_y_test, stratify=data_y_test, test_size=0.1, random_state=5, shuffle=True)

print(len(code_train))

print(len(label_train))

print(len(code_test))

print(len(label_test))

print("Showing Val")
print((label_train == 0).sum())
print((label_train == 1).sum())
print("Down showing")


print("Showing test")
print((label_test == 0).sum())
print((label_test == 1).sum())
print("Down showing")