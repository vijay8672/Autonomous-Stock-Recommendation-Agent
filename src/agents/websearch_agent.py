# Import necessary modules
import os
from dotenv import load_dotenv
from phi.model.groq import Groq
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from src.logging_setup.logger import logger

# Load environment variables
load_dotenv()

# Retrieve API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PHIDATA_API_KEY = os.getenv("PHIDATA_API_KEY")


# Ensure API keys are set
if not GROQ_API_KEY or not PHIDATA_API_KEY:
    logger.error("API keys are missing. Please check your environment variables.")

# Initialize the Groq model
groq_model = Groq(id="qwen-2.5-32b", api_key=GROQ_API_KEY)


logger.info("Creating Web Search Agent")
def web_search_agent():    
    web_agent=Agent(
        name="Web Search Agent",
        description="Searches the web for information asked by the user",
        role="Search the web for information",
        model=groq_model,
        tools=[DuckDuckGo()],
        version="0.1.0",
        instructions=[
            "always include sources",
            "use the tabular structure to display output data if required or else give the content normally"
        ],
        show_tools_calls=True)
    
    
    return web_agent

    
if __name__=="__main__":
    web_search_agent() 