import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration."""
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # We can add more configuration variables here later
    # e.g., MAX_RETRIES = 3, TIMEOUT = 30
    
config = Config()
