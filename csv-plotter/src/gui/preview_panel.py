"""
Preview Panel
Enhanced CSV data preview with statistics
"""
import tkinter as tk
from tkinter import scrolledtext, ttk


class PreviewPanel:
    """
    Enhanced preview panel showing data and statistics
    """
    
    def __init__(self, parent):
        """
        Initialize preview panel
        
        Args:
            parent: Parent widget
        """
        self.frame = tk.Frame(parent, pady=10)
        
        # ✅ FIXED: Define num_rows BEFORE create_header
        self.num_rows = tk.IntVar(value=10)
        
        # Header with title and controls
        self.create_header()
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab 1: Data Preview
        self.data_frame = tk.Frame(self.notebook)
        self.notebook.add(self.data_frame, text="📊 Data Preview")
        
        self.preview_text = scrolledtext.ScrolledText(
            self.data_frame,
            width=90,
            height=20,
            font=("Courier", 9),
            wrap=tk.NONE
        )
        self.preview_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add horizontal scrollbar for wide data
        h_scroll = tk.Scrollbar(self.data_frame, orient=tk.HORIZONTAL, command=self.preview_text.xview)
        self.preview_text.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Tab 2: Statistics
        self.stats_frame = tk.Frame(self.notebook)
        self.notebook.add(self.stats_frame, text="📈 Statistics")
        
        self.stats_text = scrolledtext.ScrolledText(
            self.stats_frame,
            width=90,
            height=20,
            font=("Courier", 9)
        )
        self.stats_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def create_header(self):
        """Create header with controls"""
        header = tk.Frame(self.frame)
        header.pack(fill=tk.X, pady=(0, 5))
        
        # Title
        title = tk.Label(
            header,
            text="Data Preview & Statistics",
            font=("Arial", 10, "bold")
        )
        title.pack(side=tk.LEFT)
        
        # Row count selector
        row_frame = tk.Frame(header)
        row_frame.pack(side=tk.RIGHT)
        
        tk.Label(row_frame, text="Show rows:", font=("Arial", 9)).pack(side=tk.LEFT, padx=(0, 5))
        
        row_spinbox = tk.Spinbox(
            row_frame,
            from_=5,
            to=100,
            increment=5,
            textvariable=self.num_rows,
            width=5,
            font=("Arial", 9)
        )
        row_spinbox.pack(side=tk.LEFT)
    
    def pack(self, **kwargs):
        """Pack the frame"""
        self.frame.pack(**kwargs)
    
    def show_preview(self, df):
        """
        Display dataframe preview
        
        Args:
            df: pandas DataFrame
        """
        if df is None:
            return
        
        # Clear previous content
        self.preview_text.delete(1.0, tk.END)
        self.stats_text.delete(1.0, tk.END)
        
        # Show data preview
        num_rows = self.num_rows.get()
        preview_data = df.head(num_rows).to_string()
        
        info_line = f"Showing first {min(num_rows, len(df))} of {len(df)} rows, {len(df.columns)} columns\n"
        info_line += "=" * 80 + "\n"
        
        self.preview_text.insert(1.0, info_line + preview_data)
        
        # Show statistics
        self.show_statistics(df)
    
    def show_statistics(self, df):
        """
        Display statistics for numeric columns
        
        Args:
            df: pandas DataFrame
        """
        stats_output = "📊 DATA STATISTICS\n"
        stats_output += "=" * 80 + "\n\n"
        
        # Basic info
        stats_output += f"Total Rows: {len(df)}\n"
        stats_output += f"Total Columns: {len(df.columns)}\n"
        stats_output += f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB\n\n"
        
        # Column types
        stats_output += "COLUMN TYPES:\n"
        stats_output += "-" * 80 + "\n"
        for col in df.columns:
            stats_output += f"  {col}: {df[col].dtype}\n"
        stats_output += "\n"
        
        # Numeric columns statistics
        numeric_cols = df.select_dtypes(include=['number']).columns
        
        if len(numeric_cols) > 0:
            stats_output += "NUMERIC COLUMNS SUMMARY:\n"
            stats_output += "-" * 80 + "\n\n"
            
            for col in numeric_cols:
                stats_output += f"📈 {col}:\n"
                stats_output += f"  Count:   {df[col].count()}\n"
                stats_output += f"  Mean:    {df[col].mean():.2f}\n"
                stats_output += f"  Median:  {df[col].median():.2f}\n"
                stats_output += f"  Std Dev: {df[col].std():.2f}\n"
                stats_output += f"  Min:     {df[col].min():.2f}\n"
                stats_output += f"  Max:     {df[col].max():.2f}\n"
                stats_output += f"  Missing: {df[col].isna().sum()}\n\n"
        
        # Non-numeric columns
        non_numeric_cols = df.select_dtypes(exclude=['number']).columns
        
        if len(non_numeric_cols) > 0:
            stats_output += "NON-NUMERIC COLUMNS SUMMARY:\n"
            stats_output += "-" * 80 + "\n\n"
            
            for col in non_numeric_cols:
                stats_output += f"📝 {col}:\n"
                stats_output += f"  Count:   {df[col].count()}\n"
                stats_output += f"  Unique:  {df[col].nunique()}\n"
                stats_output += f"  Missing: {df[col].isna().sum()}\n"
                if df[col].nunique() <= 10:
                    stats_output += f"  Values:  {', '.join(map(str, df[col].unique()[:10]))}\n"
                stats_output += "\n"
        
        self.stats_text.insert(1.0, stats_output)