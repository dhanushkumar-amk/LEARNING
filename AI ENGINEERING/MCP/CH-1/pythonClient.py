import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
import asyncio



# Path to our mcp script
mcp_script_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "firstMcpServerStdio.py")
# print(mcp_script_path)

# create server parameter
server_parameter = StdioServerParameters(
    command="python",
    args=[str(mcp_script_path)],
    env={}
)
# print(server_parameter)

# create a client ClientSession
async def main():
    async with stdio_client(server_parameter) as (read, write):

        async with ClientSession(read, write) as session:

                await session.initialize()

                # get all tools
                tools = await session.list_tools()
                print("available tools:")
                for t in tools:
                    print(t)

if __name__ == "__main__":
    asyncio.run(main())
