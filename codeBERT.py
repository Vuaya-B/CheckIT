import torch
from transformers import RobertaTokenizer, RobertaModel

# Load pre-trained CodeBERT model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaModel.from_pretrained("microsoft/codebert-base")

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

# Example code snippets
code_snippet_1 = """
def add(a, b):
    return a + b
"""

code_snippet_2 = """
def sum_two_numbers(x, y):
    return x + y
"""

similarity_score = check_plagiarism(code_snippet_1, code_snippet_2)
print(f"Similarity Score: {similarity_score}")

if similarity_score > 0.8:
    print("The code snippets are very similar and might be plagiarized.")
else:
    print("The code snippets are not similar.")
