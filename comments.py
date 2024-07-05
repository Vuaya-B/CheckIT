import os
import re

# Hard-coded file names
FILE1_NAME = 'file1.py'
FILE2_NAME = 'file2.py'

def extract_comments(code):
    single_line_comments = re.findall(r'#.*', code)
    multi_line_comments = re.findall(r'"""(.*?)"""', code, re.DOTALL) + re.findall(r"'''(.*?)'''", code, re.DOTALL)
    all_comments = single_line_comments + multi_line_comments
    return '\n'.join(comment.strip() for comment in all_comments)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    file1_path = os.path.join(current_folder, FILE1_NAME)
    file2_path = os.path.join(current_folder, FILE2_NAME)

    if not os.path.exists(file1_path):
        print(f"File {file1_path} does not exist.")
        return
    if not os.path.exists(file2_path):
        print(f"File {file2_path} does not exist.")
        return

    code_snippet_1 = read_file(file1_path)
    code_snippet_2 = read_file(file2_path)

    comments1 = extract_comments(code_snippet_1)
    comments2 = extract_comments(code_snippet_2)

    print("Comments in file1.py:\n")
    print(comments1)
    print("\n" + "="*80 + "\n")
    print("Comments in file2.py:\n")
    print(comments2)

if __name__ == "__main__":
    main()
