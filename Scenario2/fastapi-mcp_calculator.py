#HTTP
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

#1 Let's make a FastAPI app (an API) first

app = FastAPI(title="Calculator API")

@app.post("/multiply")
def multiply_numbers(a: float, b: float):
    """
    Multiplies two numbers and returns the result.
    """
    result = a * b
    return {"result": result}
@app.post("/add")
def add_numbers(a: float, b: float):
    """
    Adds two numbers and returns the result.
    """
    result = a + b
    return {"result": result}
@app.post("/subtract")
def subtract_numbers(a: float, b: float):
    """
    Subtracts the second number from the first and returns the result.
    """
    result = a - b
    return {"result": result}
@app.post("/divide")
def divide_numbers(a:float, b: float):
    """
    devides two numbers and returns the results.
    """
    if b == 0:
        return {"Error": "Division by zero not allowed."}
    result = a / b
    return {"result": result}

#2. Converting it to a MCP
mcp = FastApiMCP(app, name="Calculator MCP")
mcp.mount()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)
