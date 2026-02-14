from duckduckgo_search import DDGS

def perform_web_search(query: str, max_results: int = 3) -> str:
    """
    Searches the web and returns a formatted string of results.
    """
    try:
        results = []
        with DDGS() as ddgs:
            # We search for the query and get the top 3 results
            for r in ddgs.text(query, max_results=max_results):
                results.append(f"Source: {r['href']}\nContent: {r['body']}\n")
        
        if not results:
            return "No specific web results found."
            
        return "\n".join(results)
    except Exception as e:
        return f"Search failed: {str(e)}"