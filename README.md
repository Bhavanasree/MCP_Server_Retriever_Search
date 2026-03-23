# MCP Server: Search + Retriever

This project implements a Model Context Protocol (MCP) server using [FastMCP](https://github.com/jlowin/fastmcp). It provides tools for web searching and document retrieval/chunking, allowing AI models to access real-time web information and process long-form content.

## Features

- **Web Search**: Perform searches using DuckDuckGo to find relevant information across the web.
- **Document Retriever**: Load content from any URL and automatically split it into manageable chunks using LangChain's recursive character text splitter.

## Project Structure

```text
.
├── mcp_server.py          # Main entry point to run the MCP server
├── requirements.txt       # Project dependencies
└── src/
    ├── mcp_instance.py    # FastMCP server initialization
    └── tools/
        ├── retriever.py   # Implementation of the 'retrieve' tool
        └── web_search.py  # Implementation of the 'web_search' tool
```

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "MCP Server"
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

Start the MCP server using the following command:

```bash
python mcp_server.py
```

The server will start running on `http://localhost:8000` using the HTTP transport by default.

Add MCP server in VScode using the HTTP URL to integrate tools with VSCode copilot

## Available Tools

### `web_search(query: str, max_results: int = 5)`
Performs a web search using DuckDuckGo and returns a list of results containing titles, snippets, and URLs.

### `retrieve(url: str)`
Fetches content from the specified URL and splits it into chunks of 800 characters with a 200-character overlap, preserving the start index of each chunk.

## Dependencies

- `fastmcp`: Framework for building MCP servers.
- `langchain`: Used for document loading and text splitting.
- `duckduckgo-search`: Library for interacting with DuckDuckGo.
- `beautifulsoup4`: Used by LangChain's web loader for HTML parsing.
