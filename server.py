from fastmcp import FastMCP
import datetime

mcp = FastMCP("MyLocalTools")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together. Use this whenever the user asks for math or addition."""
    return a + b

@mcp.tool()
def get_current_time() -> str:
    """Returns the current date and time from the local system."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")