import asyncio
import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

mcp_server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "1_first_mcpserver_stdio.py")

server_param = StdioServerParameters(
    command="python",
    args=[str(mcp_server_path)],
    env={}
)

async def main():
    async with stdio_client(server_param) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", tools)

            result = await session.call_tool(
                "process",
                arguments={"path": "/path/to/data"}
            )

            print(result)

if __name__ == "__main__":
    asyncio.run(main())