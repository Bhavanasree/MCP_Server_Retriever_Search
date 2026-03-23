import asyncio
from src.mcp_instance import mcp

from src.tools.web_search import web_search
from src.tools.retriever import retrieve


async def run_mcp():
    """Function to run mcp server asynchronously"""
    await mcp.run_async(transport="http", port=8000)


if __name__ == "__main__":
   asyncio.run(run_mcp())

