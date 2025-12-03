"""
File Validation
Validates file paths and file existence
"""
import os
from src.core.config import ERROR_MESSAGES


def validate_file_path(filepath):
    """
    Check if file path is valid and file exists
    
    Args:
        filepath: Path to the file
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not filepath:
        return False, ERROR_MESSAGES["no_file"]
    
    if not os.path.exists(filepath):
        return False, ERROR_MESSAGES["file_not_exist"]
    
    if not os.path.isfile(filepath):
        return False, ERROR_MESSAGES["not_a_file"]
    
    return True, ""