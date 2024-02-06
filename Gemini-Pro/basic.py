# Import the ChatGoogleGenerativeAI class from the langchain_google_genai 
from langchain_google_genai import ChatGoogleGenerativeAI

# Option 1: Set an environment variable
# export GOOGLE_API_KEY="..."


# Option 2: Directly set the API key in the code
# llm = ChatGoogleGenerativeAI(gogle_api_key="...")

# Initialize the Gemini-Pro model using Langchain
llm = ChatGoogleGenerativeAI(model="gemini-pro" , convert_system_message_to_human=True)

# Note: If you have set your API key using the second method, use the line below
# llm = ChatGoogleGenerativeAI(openai_api_key="...") instead of the line llm = ChatGoogleGenerativeAI()

# Ask a question using the invoke method
response = llm.invoke("Put anything here that you want to ask from gemini-pro")

# Print the response
print(response)
