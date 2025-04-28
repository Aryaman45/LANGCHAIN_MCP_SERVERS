from mcp.server.fastmcp import FastMCP
import os
import requests

mcp = FastMCP("Search", port=8002)
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

@mcp.tool()
async def search(query: str) -> str:
    """Search the web for a given query using SerpAPI."""
    params = {
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "engine": "google",
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    if "error" in data:
        return f"Error: {data['error']}"
    answer_box = data.get("answer_box", {})
    if "answer" in answer_box:
        return answer_box["answer"]
    elif "snippet" in data.get("organic_results", [{}])[0]:
        return data["organic_results"][0]["snippet"]
    return "No relevant result found."

if __name__ == "__main__":
    mcp.run(transport="sse") 
