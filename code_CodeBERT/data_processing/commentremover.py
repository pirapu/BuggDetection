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
code = []


with open("/home/siddharthsa/BugDetection/Sample.java", "r") as jVfile:
    jcode = jVfile.read()
    jcode = remove_comments(jcode)
    code.append(jcode)

#codes = remove_comments(code)
print(code)