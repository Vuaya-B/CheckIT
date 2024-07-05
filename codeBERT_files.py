import os
import re
import torch
from transformers import RobertaTokenizer, RobertaModel

# Load pre-trained CodeBERT model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaModel.from_pretrained("microsoft/codebert-base")

# Hard-coded file names
FILE1_NAME = 'file1.py'
FILE2_NAME = 'file2.py'

def extract_comments(code):
    single_line_comments = re.findall(r'#.*', code)
    multi_line_comments = re.findall(r'"""(.*?)"""', code, re.DOTALL) + re.findall(r"'''(.*?)'''", code, re.DOTALL)
    all_comments = single_line_comments + multi_line_comments
    return ' '.join(comment.strip() for comment in all_comments)

def embed_code(code_snippet):
    inputs = tokenizer(code_snippet, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def calculate_similarity(embedding1, embedding2):
    cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
    return cos(embedding1, embedding2).item()

def check_plagiarism(code1, code2):
    embedding1 = embed_code(code1)
    embedding2 = embed_code(code2)
    similarity = calculate_similarity(embedding1, embedding2)
    return similarity

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

    if not comments1 or not comments2:
        print("One or both files do not contain any comments to compare.")
        return

    similarity_score = check_plagiarism(comments1, comments2)
    print(f"Similarity Score: {similarity_score}")

    if similarity_score > 0.8:
        print("The comments in the code snippets are very similar and might be plagiarized.")
    else:
        print("The comments in the code snippets are not similar.")

if __name__ == "__main__":
    main()
