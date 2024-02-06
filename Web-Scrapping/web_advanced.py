# Install required packages
# !pip install -q langchain-openai langchain playwright beautifulsoup4

# Set env var OPENAI_API_KEY or load from a .env file:
# import dotenv
# dotenv.load_dotenv()

from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Load HTML
loader = AsyncChromiumLoader(["https://www.nytimes.com/international/"])
html = loader.load()

# Transform
bs_transformer = BeautifulSoupTransformer()
docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["span"])

# Extract the content of the transformed document
x = ""
for doc in docs_transformed:
    x += doc.page_content

# Initialize the Ollama model
llm = Ollama(model="llama2")

# Create a prompt template to guide the language model's response
prompt = ChatPromptTemplate.from_messages([
    ("system", "Your task is to make the input prompt well organized. Organize the information wherever needed."),
    ("user", "{x}")
])

# Create an output parser to convert the chat message to a string
output_parser = StrOutputParser()

# Combine the prompt, language model, and output parser into a chain
chain = prompt | llm | output_parser

# Invoke the chain with an empty input (replace "" with your actual input)
response = chain.invoke({"x": x})

# Print the final response
print(response)




    
 
