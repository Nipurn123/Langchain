# Import the ChatOpenAI class from the langchain_openai module
from langchain_openai import ChatOpenAI

# Option 1: Set an environment variable
# export OPENAI_API_KEY="..."


# Option 2: Directly set the API key in the code
# llm = ChatOpenAI(openai_api_key="...")

# Initialize the OpenAI model using Langchain
llm = ChatOpenAI()

# Note: If you have set your API key using the second method, use the line below
# llm = ChatOpenAI(openai_api_key="...") instead of the line llm = ChatOpenAI()

# Ask a question using the invoke method
response = llm.invoke("Put anything here that you want to ask from chat-gpt")

# Print the response
print(response)

