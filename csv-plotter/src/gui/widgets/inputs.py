"""
Input Components
Input widget factory functions (combobox, radio buttons)
"""
import tkinter as tk
from tkinter import ttk


def create_combobox(parent, width=25, state="disabled"):
    """
    Factory method for creating comboboxes
    
    Args:
        parent: Parent widget
        width: Combobox width
        state: Combobox state
    
    Returns:
        ttk.Combobox: Configured combobox
    """
    combobox = ttk.Combobox(parent, width=width, state=state)
    return combobox


def create_radio_button(parent, text, variable, value, font_size=9):
    """
    Factory method for creating radio buttons
    
    Args:
        parent: Parent widget
        text: Radio button text
        variable: tk Variable
        value: Radio button value
        font_size: Font size
    
    Returns:
        tk.Radiobutton: Configured radio button
    """
    radio = tk.Radiobutton(
        parent,
        text=text,
        variable=variable,
        value=value,
        font=("Arial", font_size)
    )
    
    return radio