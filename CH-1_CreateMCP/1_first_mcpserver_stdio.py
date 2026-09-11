from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
async def fetch():
    """Use this tool to fetch from a source

    You can make some API calls here or fetch data from a database
    """
    return {"data": "Hello, MCP"}

@mcp.tool()
async def process(path: str):
    """Use this tool to process the fetching of data

    Args:
        It takes path as an arguement

    Returns:
        It returns a dict with the path
    """
    return {"processed_data": "Data has been processed! at path: " + path}

if __name__ == "__main__":
    mcp.run(transport="stdio")
