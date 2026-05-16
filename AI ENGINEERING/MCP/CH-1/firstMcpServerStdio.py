from fastmcp import FastMCP

# create the object
mcp = FastMCP()


# first mcp server
@mcp.tool()
def fetch():
    """use this tool to fetch the data from the server"""
    return "Hello world this is your MCP server"

@mcp.tool()
def process(name:str):
    """use this tool to process the data from the server"""
    return f"Hello {name} this is your MCP server"

# run the mcp server with stdio 
if __name__ == "__main__":
    mcp.run(transport="stdio")
