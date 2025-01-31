from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv

# Load environment variables (like your OpenAI API key)
load_dotenv()

async def main():
    # Ask user for the task they want to automate
    user_task = input("Enter the task you want to automate: ")
    
    # Initialize the agent with the user-provided task
    agent = Agent(
        task=user_task,
        llm=ChatOpenAI(model="gpt-4o-mini"),
    )
    
    # Run the agent to process the task
    result = await agent.run()
    
    # Print the result
    print(result)

# Run the main function
asyncio.run(main())
