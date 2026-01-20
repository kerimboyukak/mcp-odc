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

@mcp.tool()
def calculate_vat(price: float, rate: float = 21.0) -> str:
    """Calculates the VAT amount. Use this for all price and tax questions."""
    amount = price * (rate / 100)
    total = price + amount
    return f"The VAT is {amount:.2f} and the total price is {total:.2f}"

@mcp.tool()
def get_shouty_version(text: str) -> str:
    """Converts a message to all uppercase. Use this only if the user asks for 'urgent' or 'shouty' output."""
    return text.upper()

@mcp.tool()
def get_order_status(order_id: str) -> str:
    """Returns the shipping status of an order ID. Use this for order tracking."""
    # Dummy data simulating a database lookup
    orders = {"ORD-123": "Shipped", "ORD-456": "Processing", "ORD-789": "Delivered"}
    return orders.get(order_id, "Order ID not found in system.")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")