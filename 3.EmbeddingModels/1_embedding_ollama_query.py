
from langchain_ollama import OllamaEmbeddings

# Initialize your local Ollama embedding model
embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Generate an embedding for a single query
result = embedding.embed_query(
    "Delhi is the capital of India"
)

# Print the embedding vector
print("Vector")
print(str(result))
