from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router

# Initialize the FastAPI application
app = FastAPI(
    title="AI-Powered Personalized Cold Email Generator",
    description="Backend API for automating company research and email generation.",
    version="1.0.0"
)

# Setup CORS (Cross-Origin Resource Sharing)
# This is required because our Streamlit frontend will run on a different port (usually 8501)
# than our FastAPI backend (usually 8000), and browsers block requests between different ports by default.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, this should be specific origins (e.g. ["http://localhost:8501"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API routes defined in api/routes.py
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    # This block allows us to run the server directly by executing this file
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
