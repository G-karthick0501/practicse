import tkinter as tk
from tkinter import scrolledtext, messagebox
from src.core.config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT
from src.core.charts import create_line_chart, create_bar_chart
from src.utils.validators import validate_column_selection, validate_numeric_data
from src.gui.widgets import (
    create_button, create_label, create_combobox, 
    create_radio_button, create_frame
)
from src.gui.file_handler import FileHandler
from src.gui.status_bar import StatusBar
from src.gui.preview_panel import PreviewPanel
class MainWindow:
    """
    Main application window
    Now follows Single Responsibility Principle - only orchestrates UI
    All business logic delegated to specialized modules
    """
    
    def __init__(self, root):
        """Initialize the main window"""
        self.root = root
        self.file_handler = FileHandler()  # Dependency injection
        self.chart_window = None
        self.setup_window()
        self.create_ui()
    
    def setup_window(self):
        """Setup basic window properties"""
        self.root.title(APP_NAME)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        
        # Center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
    
    def create_ui(self):
        """Create all UI components using factory methods"""
        # File section
        self.create_file_section()
        
        # Column selection section
        self.create_column_section()
        
        # Chart type section
        self.create_chart_type_section()
        
        # Generate button
        self.create_generate_button()
        
        # Preview section - NEW ENHANCED VERSION
        self.preview_panel = PreviewPanel(self.root)
        self.preview_panel.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Status bar
        self.status_bar = StatusBar(self.root)

    def create_file_section(self):
        """Create file selection section"""
        file_frame = create_frame(self.root, padding=20)
        file_frame.pack()
        
        self.browse_btn = create_button(
            file_frame,
            text="Browse CSV File",
            command=self.handle_browse,
            width=20,
            height=2
        )
        self.browse_btn.pack()
    
    def create_column_section(self):
        """Create column selection section"""
        column_frame = create_frame(self.root, padding=10)
        column_frame.pack()
        
        # X-axis
        x_label = create_label(column_frame, "X-axis Column:", font_size=10)
        x_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        
        self.x_column_combo = create_combobox(column_frame, width=25, state="disabled")
        self.x_column_combo.grid(row=0, column=1, padx=10, pady=5)
        
        # Y-axis
        y_label = create_label(column_frame, "Y-axis Column:", font_size=10)
        y_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        self.y_column_combo = create_combobox(column_frame, width=25, state="disabled")
        self.y_column_combo.grid(row=1, column=1, padx=10, pady=5)
    
    def create_chart_type_section(self):
        """Create chart type selection section"""
        column_frame = self.root.winfo_children()[1]  # Get column frame
        
        chart_type_label = create_label(column_frame, "Chart Type:", font_size=10)
        chart_type_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        
        radio_frame = create_frame(column_frame, padding=0)
        radio_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        self.chart_type = tk.StringVar(value="line")
        
        line_radio = create_radio_button(
            radio_frame, "Line Chart", self.chart_type, "line"
        )
        line_radio.pack(side=tk.LEFT, padx=5)
        
        bar_radio = create_radio_button(
            radio_frame, "Bar Chart", self.chart_type, "bar"
        )
        bar_radio.pack(side=tk.LEFT, padx=5)
    
    def create_generate_button(self):
        """Create generate chart button"""
        column_frame = self.root.winfo_children()[1]  # Get column frame
        
        self.generate_btn = create_button(
            column_frame,
            text="Generate Chart",
            command=self.handle_generate,
            width=20,
            height=2,
            state="disabled",
            style="primary"
        )
        self.generate_btn.grid(row=3, column=0, columnspan=2, pady=15)
    
    # ===== Event Handlers =====
    
    def handle_browse(self):
        """Handle file browse action"""
        self.status_bar.set_info("Browsing for file...")
        
        # Get file path
        filepath = self.file_handler.browse_file()
        
        if not filepath:
            self.status_bar.clear()
            return
        
        # Load file
        self.status_bar.set_info(f"Loading: {filepath}")
        success, result = self.file_handler.load_file(filepath)
        
        if not success:
            messagebox.showerror("Error", result)
            self.status_bar.set_error("Failed to load file")
            return
        
        # Success - update UI
        self.status_bar.set_success(f"Loaded: {self.file_handler.current_file}")
        self.update_ui_after_load()
    
    def update_ui_after_load(self):
        """Update UI elements after successful file load"""
        # Show preview with new panel
        self.preview_panel.show_preview(self.file_handler.get_dataframe())
        
        # Populate dropdowns
        columns = self.file_handler.get_columns()
        
        self.x_column_combo['values'] = columns
        self.x_column_combo['state'] = 'readonly'
        if columns:
            self.x_column_combo.current(0)
        
        self.y_column_combo['values'] = columns
        self.y_column_combo['state'] = 'readonly'
        if len(columns) > 1:
            self.y_column_combo.current(1)
        elif columns:
            self.y_column_combo.current(0)
        
        # Enable generate button
        self.generate_btn['state'] = 'normal'
        
        print(f"File loaded: {self.file_handler.current_file}")
        print(f"Columns: {columns}")

    def handle_generate(self):
        """Handle chart generation action"""
        df = self.file_handler.get_dataframe()
        
        if df is None:
            messagebox.showerror("Error", "No data loaded")
            return
        
        # Get selections
        x_column = self.x_column_combo.get()
        y_column = self.y_column_combo.get()
        
        # Validate column selection
        is_valid, error_message = validate_column_selection(x_column, y_column)
        if not is_valid:
            messagebox.showerror("Error", error_message)
            self.status_bar.set_error("Invalid column selection")
            return
        
        # Validate numeric data
        is_valid, error_message = validate_numeric_data(df, y_column)
        if not is_valid:
            messagebox.showerror("Error", error_message)
            self.status_bar.set_error("Y-axis must be numeric")
            return
        
        # Generate chart
        chart_type = self.chart_type.get()
        self.status_bar.set_info(f"Generating {chart_type} chart...")
        
        try:
            if chart_type == "line":
                self.chart_window = create_line_chart(df, x_column, y_column)
                self.status_bar.set_success(f"Line chart generated: {y_column} vs {x_column}")
            elif chart_type == "bar":
                self.chart_window = create_bar_chart(df, x_column, y_column)
                self.status_bar.set_success(f"Bar chart generated: {y_column} vs {x_column}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate chart: {str(e)}")
            self.status_bar.set_error("Chart generation failed")
