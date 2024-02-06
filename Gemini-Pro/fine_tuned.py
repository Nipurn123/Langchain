# Import necessary classes and functions
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(model="gemini-pro" , convert_system_message_to_human=True)

# Create a prompt template to guide the language model's response
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class technical documentation writer."),
    ("user", "{input}")
])

# Create an output parser to convert the chat message to a string
output_parser = StrOutputParser()

# Combine the prompt, language model, and output parser into a chain
chain = prompt | llm | output_parser 

# Invoke the chain with an empty input (replace "" with your actual input)
response = chain.invoke({"input": "Ask anything that you wannt to ask."})

# Print the final response
print(response)
