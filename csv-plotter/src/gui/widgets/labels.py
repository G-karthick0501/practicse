"""
Label Components
Label factory functions
"""
import tkinter as tk


def create_label(parent, text, font_size=10, bold=False, anchor="w"):
    """
    Factory method for creating styled labels
    
    Args:
        parent: Parent widget
        text: Label text
        font_size: Font size
        bold: Bold text
        anchor: Text anchor
    
    Returns:
        tk.Label: Configured label
    """
    font_weight = "bold" if bold else "normal"
    
    label = tk.Label(
        parent,
        text=text,
        font=("Arial", font_size, font_weight),
        anchor=anchor
    )
    
    return label