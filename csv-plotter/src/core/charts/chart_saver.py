"""
Chart Saver
Handles saving/exporting charts to files
"""
from tkinter import filedialog, messagebox


def save_chart(figure, default_name="chart"):
    """
    Save matplotlib figure to file
    
    Args:
        figure: Matplotlib figure object
        default_name: Default filename
    
    Returns:
        bool: True if saved successfully
    """
    filepath = filedialog.asksaveasfilename(
        defaultextension=".png",
        initialfile=default_name,
        filetypes=[
            ("PNG Image", "*.png"),
            ("PDF Document", "*.pdf"),
            ("JPEG Image", "*.jpg"),
            ("SVG Vector", "*.svg")
        ],
        title="Save Chart As"
    )
    
    if not filepath:
        return False
    
    try:
        # Save with high quality
        figure.savefig(
            filepath,
            dpi=300,
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none'
        )
        messagebox.showinfo("Success", f"Chart saved to:\n{filepath}")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save chart:\n{str(e)}")
        return False