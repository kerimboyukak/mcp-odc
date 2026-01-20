from fastmcp import FastMCP
import datetime

mcp = FastMCP("MyLocalTools")


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
    """Returns shipping status. Use this whenever an order ID is mentioned."""
    clean_id = order_id.strip().upper()
    
    if not clean_id.startswith("ORD-"):
        clean_id = f"ORD-{clean_id}"
        
    orders = {"ORD-123": "Shipped", "ORD-456": "Processing", "ORD-789": "Delivered"}
    
    return orders.get(clean_id, f"Error: Order {clean_id} not found in our records.")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")