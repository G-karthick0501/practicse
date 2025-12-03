"""
Data Validation
Validates dataframes and data content
"""
import pandas as pd
from src.core.config import ERROR_MESSAGES


def validate_dataframe(df):
    """
    Check if dataframe is valid and not empty
    
    Args:
        df: pandas DataFrame
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if df is None:
        return False, ERROR_MESSAGES["no_data"]
    
    if df.empty:
        return False, ERROR_MESSAGES["empty_csv"]
    
    if len(df.columns) == 0:
        return False, ERROR_MESSAGES["no_columns"]
    
    return True, ""


def validate_column_selection(x_column, y_column):
    """
    Validate that selected columns are different
    
    Args:
        x_column: Selected X-axis column
        y_column: Selected Y-axis column
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not x_column or not y_column:
        return False, ERROR_MESSAGES["no_column_selected"]
    
    if x_column == y_column:
        return False, ERROR_MESSAGES["same_columns"]
    
    return True, ""


def validate_numeric_data(df, y_column):
    """
    Validate that Y column contains numeric data
    
    Args:
        df: pandas DataFrame
        y_column: Column name for Y-axis
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if y_column not in df.columns:
        return False, f"Column '{y_column}' not found in data"
    
    # Check if column is numeric
    if not pd.api.types.is_numeric_dtype(df[y_column]):
        return False, ERROR_MESSAGES["y_not_numeric"]
    
    return True, ""