"""
Error and Status Messages
Centralized message strings
"""

ERROR_MESSAGES = {
    "no_file": "No file selected. Please choose a CSV file.",
    "file_not_exist": "The selected file does not exist.",
    "not_a_file": "The selected path is not a valid file.",
    "no_data": "No data has been loaded yet.",
    "empty_csv": "The CSV file is empty. Please select a file with data.",
    "no_columns": "The CSV file has no columns.",
    "same_columns": "X-axis and Y-axis cannot be the same column. Please select different columns.",
    "no_column_selected": "Please select columns for both X-axis and Y-axis.",
    "y_not_numeric": "Y-axis column must contain numeric data. Please select a different column.",
}

STATUS_MESSAGES = {
    "ready": "Ready",
    "browsing": "Browsing for file...",
    "loading": "Loading file...",
    "loaded": "File loaded successfully",
    "generating": "Generating chart...",
}