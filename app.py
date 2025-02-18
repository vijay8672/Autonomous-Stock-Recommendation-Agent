from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from src.logging_setup.logger import logger
from src.agents.multi_agent import MultiAgent  # Importing MultiAgent class
import os
from fastapi.responses import JSONResponse  # For structured response

# Load environment variables
load_dotenv()

# Retrieve API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PHIDATA_API_KEY = os.getenv("PHIDATA_API_KEY")

# Ensure API keys are set
if not GROQ_API_KEY or not PHIDATA_API_KEY:
    logger.error("API keys are missing. Please check your environment variables.")
    raise ValueError("API keys are missing. Please check your environment variables.")

# Initialize FastAPI app
app = FastAPI(title="Autonomous Financial Advisor Agent", version="0.1.0")

# Instantiate MultiAgent only once
multi_agent_instance = MultiAgent()

# Request model for FastAPI
class QueryRequest(BaseModel):
    query: str

# Route to check API status
@app.get("/status")
def status():
    return {"status": "API is running"}

# Route to handle Multi-Agent queries
@app.post("/query")
def query_agent(data: QueryRequest):
    try:
        result = multi_agent_instance.run(data.query)
        return result  # Return only the result
    except NameError as name_err:
        logger.error(f"NameError: {name_err}")
        raise HTTPException(status_code=500, detail="Internal Server Error: NameError encountered.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Main block to run FastAPI using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
