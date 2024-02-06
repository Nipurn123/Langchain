# Import the Ollama class from the langchain_community.llms module
from langchain_community.llms import Ollama

# Initialize the Ollama model using the "llama2" model
llm = Ollama(model="llama2")

# Ask a question using the invoke method
response = llm.invoke("Put anything here that you want to ask from Ollama")

# Print the response
print(response)
