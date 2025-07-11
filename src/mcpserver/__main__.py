from mcpserver.weather import mcp

def main():
    mcp.run()

# avoid first import execution
if __name__ == "__main__":
    main()