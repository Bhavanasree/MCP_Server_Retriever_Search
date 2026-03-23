import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.mcp_instance import mcp

url="https://docs.langchain.com/oss/python/langchain/rag#build-a-rag-agent-with-langchain"

@mcp.tool
def retrieve(url: str):
    """ Retrieve content from a URL."""
    print(f"DEBUG: Retrieving content from URL='{url}'")
    loader = WebBaseLoader(
        web_paths=(url,)
    )
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200,
        add_start_index=True,
    )
    return text_splitter.split_documents(docs)
