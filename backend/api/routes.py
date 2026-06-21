from fastapi import APIRouter

# Create an APIRouter instance
router = APIRouter()

@router.get("/health", tags=["System"])
async def health_check():
    """
    Check if the API server is running correctly.
    """
    return {
        "status": "online",
        "service": "AI Cold Email Generator API"
    }

# Stubs for endpoints we will build in upcoming days
@router.post("/upload", tags=["Data Processing"])
async def upload_excel():
    """
    Endpoint to handle Excel file uploads.
    """
    return {"message": "Upload endpoint - To be implemented"}

@router.post("/process", tags=["AI Processing"])
async def process_leads():
    """
    Endpoint to trigger the AI processing of leads.
    """
    return {"message": "Process endpoint - To be implemented"}

@router.get("/download", tags=["Data Processing"])
async def download_results():
    """
    Endpoint to download the processed Excel file.
    """
    return {"message": "Download endpoint - To be implemented"}
