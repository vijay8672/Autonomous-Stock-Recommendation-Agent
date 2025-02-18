# Import necessary modules
import os
from dotenv import load_dotenv
from src.logging_setup.logger import logger
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.openbb_tools import OpenBBTools


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


# Initialize Financial Agent
logger.info("Creating Financial Agent")

def financial_agent():
    finance_agent = Agent(
        name="Stock Financial Advisor Agent",
        description="You are an investment analyst, researches stock prices, analyst recommendations, and stock fundamentals and stock related news.",
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

    return finance_agent
logger.info("Created Financial Agent")

    
    
if __name__=="__main__":
    financial_agent()