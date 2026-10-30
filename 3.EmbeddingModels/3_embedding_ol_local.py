
from langchain_ollama import OllamaEmbeddings

# Initialize the local Ollama embedding model
embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Documents to convert into numerical vectors
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Generate embeddings for all documents
vectors = embedding.embed_documents(documents)

# Print the number of documents and vector dimensions
print("Number of documents:", len(vectors))
# print("Dimensions of first vector:", len(vectors[0]))

# Print the generated vectors
print(vectors)
