from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
async def fetch_http():
    """Use this tool to fetch data from a source
    You can make some API calls here or fetch data from a database
    """
    return {"data": "Hello, MCP"}

@mcp.tool()
async def process_http(path: str):
    '''Use this tool to process the fetched data.'''

    # Simulate processing the fetched data
    ''' You can perform some data transformations here '''
    return {"processed_data": "Data has been processed! at path: " + path}

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port= 8050)