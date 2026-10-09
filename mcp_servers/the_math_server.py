from mcp.server.mcpserver import MCPServer

mcp: MCPServer = MCPServer("MathServer")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b


@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers together. Both inputs must be plain numbers like 7, not calculations like 3 + 4. If a number still has to be calculated, call add_numbers first and use its result."""
    return a * b


if __name__ == "__main__":
    # Force SSE transport to bypass Windows stdio pipe limits
    print("🚀 Starting Math Server on http://127.0.0.1:54321/sse ...")
    # The host and port are set when the server starts
    mcp.run(transport="sse", host="127.0.0.1", port=54321)
