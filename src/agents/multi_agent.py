import os
from dotenv import load_dotenv
from src.logging_setup.logger import logger
from phi.model.groq import Groq
from src.agents.websearch_agent import web_search_agent
from src.agents.finance_agent import financial_agent
from phi.agent import Agent

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

class MultiAgent:
    def __init__(self):
        logger.info("Creating Multi AI Agent")
        self.websearch_agent = web_search_agent()  # Initialize web search agent
        self.finance_agent = financial_agent()  # Initialize finance agent
        logger.info("Agents are created successfully")

    def multi_ai_agent(self):
        # Create multi-agent instance with necessary tools and instructions
        multi_agent = Agent(
            team=[self.websearch_agent, self.finance_agent],
            model=groq_model,
            description="A multi-agent accessing multiple AI agents.",
            instructions=[
                "Format your response using markdown, use table to display the data.",
                "Always include sources."
            ],
            show_tools_calls=True,
            markdown=True
        )
        return multi_agent

    # Method to interact with the multi-agent and handle responses
    def run(self, query):
        try:
            multiai_agent = self.multi_ai_agent()  # Initialize multi-agent
            
            response = multiai_agent.print_response(query)  # This method might be 'query()' or similar
            
            return response  # Print the response from the multi-agent
            
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            print(f"Error Details: {str(e)}")

if __name__ == "__main__":
    query = "NVDA stock"
    multi_agent = MultiAgent()  # Create the multi-agent instance
    multi_agent.run(query)
