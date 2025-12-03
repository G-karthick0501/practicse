"""
Chart Base
Common chart functionality and utilities
"""
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from src.core.config import CHART_SETTINGS


def create_chart_window(title, width=None, height=None):
    """
    Create a new window for displaying a chart
    
    Args:
        title: Window title
        width: Window width (optional)
        height: Window height (optional)
    
    Returns:
        tk.Toplevel: New window
    """
    window = tk.Toplevel()
    window.title(title)
    
    w = width or CHART_SETTINGS['window_width']
    h = height or CHART_SETTINGS['window_height']
    window.geometry(f"{w}x{h}")
    
    return window


def embed_chart_in_window(figure, window, chart_name="chart"):
    """
    Embed a matplotlib figure in a tkinter window with toolbar and save button
    
    Args:
        figure: Matplotlib figure
        window: Tkinter window
        chart_name: Name for saving the chart
    
    Returns:
        canvas: Figure canvas
    """
    # Create frame for chart
    chart_frame = tk.Frame(window)
    chart_frame.pack(fill='both', expand=True)
    
    # Embed canvas
    canvas = FigureCanvasTkAgg(figure, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True, padx=10, pady=10)
    
    # Add navigation toolbar
    toolbar = NavigationToolbar2Tk(canvas, chart_frame)
    toolbar.update()
    
    # Add custom save button frame at bottom
    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
    
    def save_chart_handler():
        from src.core.charts.chart_saver import save_chart
        save_chart(figure, default_name=chart_name)
    
    save_btn = tk.Button(
        button_frame,
        text="💾 Save Chart",
        command=save_chart_handler,
        font=("Arial", 10, "bold"),
        bg="#4CAF50",
        fg="white",
        width=15,
        height=1
    )
    save_btn.pack(side=tk.RIGHT, padx=5)
    
    info_label = tk.Label(
        button_frame,
        text="Use toolbar to zoom, pan, or click 'Save Chart' to export",
        font=("Arial", 9),
        fg="gray"
    )
    info_label.pack(side=tk.LEFT, padx=5)
    
    return canvas


def apply_common_styling(ax, x_column, y_column, title):
    """
    Apply common styling to chart axes
    
    Args:
        ax: Matplotlib axis
        x_column: X-axis label
        y_column: Y-axis label
        title: Chart title
    """
    import matplotlib.pyplot as plt
    
    # Labels
    ax.set_xlabel(
        x_column, 
        fontsize=CHART_SETTINGS['label_fontsize'], 
        fontweight='bold'
    )
    ax.set_ylabel(
        y_column, 
        fontsize=CHART_SETTINGS['label_fontsize'], 
        fontweight='bold'
    )
    ax.set_title(
        title,
        fontsize=CHART_SETTINGS['title_fontsize'],
        fontweight='bold',
        pad=CHART_SETTINGS['title_pad']
    )
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()