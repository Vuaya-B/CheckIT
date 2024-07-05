import torch
from transformers import RobertaTokenizer, RobertaModel

# Load pre-trained CodeBERT model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaModel.from_pretrained("microsoft/codebert-base")

def embed_text(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def calculate_similarity(embedding1, embedding2):
    cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
    return cos(embedding1, embedding2).item()

text1 = """
# Function to greet the user
# Function to bid farewell to the user
# Main function to demonstrate greeting and farewell
# Example user name
# Call the greeting function
# Call the farewell function
# Entry point of the program
"""

text2 = """
# Function to calculate the square of a number
# Function to calculate the cube of a number
# Main function to demonstrate square and cube calculations
# Example number to calculate square and cube
# Call the square function
# Call the cube function
# Entry point of the program
"""

embedding1 = embed_text(text1)
embedding2 = embed_text(text2)
similarity_score = calculate_similarity(embedding1, embedding2)
print(f"Similarity Score: {similarity_score:.2f}")
