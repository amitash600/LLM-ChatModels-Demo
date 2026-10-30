
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="codellama:7b",
    temperature=0.5,
    num_predict=100
)

result = model.invoke("Write 5 lines poem on cricket.")

print(result.content)
