import requests
from ddgs import DDGS
import sys
import json
from src.mcp_instance import mcp


@mcp.tool
def web_search(query: str,max_results: int = 5):
    """Perform the web search using the DuckDuckGo and return the JSON results."""
    try:
        result=[]
        with DDGS() as ddgs:
            ddgs_gen=ddgs.text(query,region='wt-wt', safesearch='moderate', max_results=max_results)
            for r in ddgs_gen:
                result.append(r)
        return result
    
        if not result:
            return "No results found."
        
        return json.dumps(result, indent=2)
    
    except Exception as e:

        error_msg = f"Search failed: {str(e)}"
        print(error_msg)
        return error_msg 
