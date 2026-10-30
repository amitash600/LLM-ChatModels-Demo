
from langchain_ollama import ChatOllama

# Initialize the local Ollama chat model
llm = ChatOllama(
    model="codellama:7b",
    temperature=0
)

# Send a prompt to the model
result = llm.invoke("What is the capital of India?")

# Print the response
print(result.content)
