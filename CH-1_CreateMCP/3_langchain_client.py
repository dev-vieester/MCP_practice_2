from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os

mcp_server_path = os.path.join((os.path.dirname(os.path.abspath(__file__))), "1_first_mcpserver_stdio.py")

venv_path = os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".venv")

async def main():
    client = MultiServerMCPClient(
        {
            "data_fetch_mcp_stdio":{
                "transport": "stdio",
                "command": os.path.join(venv_path, "Scripts", "python.exe"),
                "args": [str(mcp_server_path)]
            }
        }
    )

    tools = await client.get_tools()
    print("Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())