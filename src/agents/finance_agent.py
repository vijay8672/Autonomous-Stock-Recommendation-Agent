# Import necessary modules
import os
from dotenv import load_dotenv
from src.logging_setup.logger import logger
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.openbb_tools import OpenBBTools
import time


# Load environment variables
load_dotenv()

# Retrieve API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PHIDATA_API_KEY = os.getenv("PHIDATA_API_KEY")


# Ensure API keys are set
if not GROQ_API_KEY or not PHIDATA_API_KEY:
    logger.error("API keys are missing. Please check your environment variables.")

# Initialize the Groq model
groq_model = Groq(id="llama3-8b-8192", api_key=GROQ_API_KEY)


# Initialize Financial Agent
logger.info("Creating Financial Agent")

def financial_agent(query):
    try:
        finance_agent = Agent(
            name="Stock Financial Advisor Agent",
            description="You are an investment analyst, researching stock prices, analyst recommendations, and stock fundamentals.",
            model=groq_model,
            tools=[
                YFinanceTools(
                    stock_price=True,
                    analyst_recommendations=True,
                    stock_fundamentals=True,
                    company_news=True,
                    company_info=True,
                    historical_prices=True,
                )
            ],
            instructions=["Format your response using markdown and use tables to display data where possible."],
            show_tools_calls=True,
            markdown=True
            )

        response = finance_agent.print_response(query)
        return response
        

    except Exception as e:
        logger.error(f"Error fetching stock data: {e}")




# Run the query
if __name__ == "__main__":
    query = "NVDA stock current market price"
    print(financial_agent(query))
