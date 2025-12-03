"""
CSV Handler
Loads and processes CSV files
"""
import pandas as pd

def load_csv(filepath):
    """
    Load CSV file using pandas
    No validation yet - just basic loading
    """
    df = pd.read_csv(filepath)
    return df


def get_columns(df):
    """
    Get list of column names from dataframe
    
    Args:
        df: pandas DataFrame
        
    Returns:
        list: Column names
    """
    if df is None:
        return []
    return list(df.columns)