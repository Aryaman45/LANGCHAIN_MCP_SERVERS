import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
load_dotenv()

# Mapping server names to their ports
SERVER_PORTS = {
    "math": 8001,
    "search": 8002,
    "weather":8000
}

async def main():
    # Fetch OpenAI API Key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("Error: OPENAI_API_KEY is not set in the environment.")
        return

    print("Available servers: ", list(SERVER_PORTS.keys()))
    selected_servers = input("Enter servers you want to connect to (comma-separated, e.g., math,search): ")
    selected_servers = [s.strip() for s in selected_servers.split(",") if s.strip()]

    connections = {}
    for server in selected_servers:
        port = SERVER_PORTS.get(server)
        if port:
            connections[server] = {
                "url": f"http://localhost:{port}/sse",
                "transport": "sse",
            }
        else:
            print(f"Warning: Unknown server '{server}', skipping.")

    if not connections:
        print("No valid servers selected. Exiting.")
        return

    user_prompt = input("Enter your question/prompt: ")

    model = ChatOpenAI(model="gpt-4o", openai_api_key=openai_api_key)

    async with MultiServerMCPClient(connections) as client:
        agent = create_react_agent(model, client.get_tools())

        response = await agent.ainvoke({"messages": user_prompt})

        messages = response['messages']
        final_answer = None
        for msg in reversed(messages):
            if msg.__class__.__name__ == "AIMessage" and msg.content.strip():
                final_answer = msg.content
                break

        print("\n==============================")
        print("Final Answer:", final_answer)
        print("==============================")

asyncio.run(main())
