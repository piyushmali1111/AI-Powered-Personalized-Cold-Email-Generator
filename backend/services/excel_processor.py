import pandas as pd
import os
from io import BytesIO

# The columns we expect in the uploaded Excel file
REQUIRED_COLUMNS = ["lead_name", "company_name", "website", "email"]

def validate_excel(df: pd.DataFrame) -> tuple[bool, str]:
    """
    Validates that the uploaded DataFrame contains the required columns.
    
    Args:
        df: Pandas DataFrame representing the uploaded Excel file.
        
    Returns:
        tuple (is_valid: bool, error_message: str)
    """
    # Check for missing columns
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    
    if missing_columns:
        return False, f"Missing required columns: {', '.join(missing_columns)}"
        
    # Check if the dataframe is empty
    if df.empty:
        return False, "The uploaded file is empty."
        
    # Check if there are any rows where the website is missing (we need it for scraping)
    # We check if the column exists first (handled by missing_columns check above)
    if df["website"].isnull().all():
        return False, "All rows are missing website URLs."
        
    return True, ""

def process_upload(file_content: bytes) -> tuple[pd.DataFrame | None, str]:
    """
    Reads the bytes of an uploaded Excel file and validates it.
    
    Args:
        file_content: Raw bytes of the uploaded file.
        
    Returns:
        tuple (dataframe: pd.DataFrame or None, error_message: str)
    """
    try:
        # Read the Excel file into a Pandas DataFrame
        # BytesIO is used to read from memory instead of a file on disk
        df = pd.read_excel(BytesIO(file_content))
        
        is_valid, error_msg = validate_excel(df)
        
        if not is_valid:
            return None, error_msg
            
        # Clean the data: Fill NaN values with empty strings
        df = df.fillna("")
        
        # Add new columns that we will populate later using AI
        new_columns = [
            "company_summary", "industry", "services", "target_audience",
            "unique_selling_points", "email_subject", "email_body", 
            "processing_status", "error_message"
        ]
        
        for col in new_columns:
            if col not in df.columns:
                df[col] = ""
                
        return df, ""
        
    except Exception as e:
        return None, f"Failed to read Excel file: {str(e)}"

def export_to_excel(df: pd.DataFrame, file_path: str) -> bool:
    """
    Exports a Pandas DataFrame to an Excel file.
    
    Args:
        df: The DataFrame to export.
        file_path: The path where the file should be saved.
        
    Returns:
        bool indicating success
    """
    try:
        df.to_excel(file_path, index=False)
        return True
    except Exception as e:
        print(f"Error exporting to Excel: {e}")
        return False
