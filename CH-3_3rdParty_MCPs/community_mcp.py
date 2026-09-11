from langchain_mcp_adapters.client import MultiServerMCPClient
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "mcp-server-firecrawl": {
                "transport": "streamable-http",
                "url": "https://mcp.firecrawl.dev/v2/mcp",
                "headers": {
                    "Authorization": f"Bearer {os.getenv("FIRECRAWL_API_KEY")}"
                }
            },
        }
    )

    tools = await client.get_tools()
    print("Available tools:", len(tools))
    fetch_tool = tools[0]
    result = await fetch_tool.ainvoke({"url": "https://www.xedla.com/"})
    print("Tool result:", result)



if __name__ == "__main__":
    asyncio.run(main())