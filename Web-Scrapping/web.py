#pip install -q langchain-openai langchain playwright beautifulsoup4
#pip install  playwright install


# Set env var OPENAI_API_KEY or load from a .env file:
# import dotenv
# dotenv.load_dotenv()



from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer


# Load HTML

loader = AsyncChromiumLoader(["https://python.langchain.com/docs/get_started/introduction"])

html = loader.load()
print(html)
