"""
File Handler
Handles file operations separately from UI
Follows Single Responsibility Principle
"""
from tkinter import filedialog, messagebox
from src.core.csv_handler import load_csv, get_columns
from src.utils.validators import validate_file_path, validate_dataframe 


class FileHandler:
    """
    Handles all file-related operations
    Decoupled from UI following Dependency Inversion Principle
    """
    
    def __init__(self):
        """Initialize file handler"""
        self.current_file = None
        self.dataframe = None
    
    def browse_file(self):
        """
        Open file dialog and return selected filepath
        
        Returns:
            str: Selected filepath or None
        """
        filepath = filedialog.askopenfilename(
            title="Select a CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        return filepath
    
    def load_file(self, filepath):
        """
        Load and validate CSV file
        
        Args:
            filepath: Path to CSV file
        
        Returns:
            tuple: (success, dataframe or error_message)
        """
        # Validate file path
        is_valid, error_message = validate_file_path(filepath)
        if not is_valid:
            return False, error_message
        
        # Load CSV
        try:
            df = load_csv(filepath)
        except Exception as e:
            return False, f"Failed to load CSV: {str(e)}"
        
        # Validate dataframe
        is_valid, error_message = validate_dataframe(df)
        if not is_valid:
            return False, error_message
        
        # Store successful load
        self.current_file = filepath
        self.dataframe = df
        
        return True, df
    
    def get_columns(self):
        """
        Get column names from loaded dataframe
        
        Returns:
            list: Column names or empty list
        """
        if self.dataframe is not None:
            return get_columns(self.dataframe)
        return []
    
    def get_preview_text(self, num_rows=5):
        """
        Get preview text of dataframe
        
        Args:
            num_rows: Number of rows to preview
        
        Returns:
            str: Preview text
        """
        if self.dataframe is not None:
            return self.dataframe.head(num_rows).to_string()
        return ""
    
    def get_dataframe(self):
        """
        Get the current dataframe
        
        Returns:
            DataFrame: Current dataframe or None
        """
        return self.dataframe