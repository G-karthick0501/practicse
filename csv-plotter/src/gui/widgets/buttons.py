"""
Button Components
Button factory functions
"""
import tkinter as tk
from src.core.config import COLORS


def create_button(parent, text, command, width=20, height=2, state="normal", style="default"):
    """
    Factory method for creating styled buttons
    
    Args:
        parent: Parent widget
        text: Button text
        command: Button command
        width: Button width
        height: Button height
        state: Button state
        style: Button style ('default' or 'primary')
    
    Returns:
        tk.Button: Configured button
    """
    if style == "primary":
        bg_color = COLORS['primary']
        fg_color = COLORS['button_text']
        font = ("Arial", 10, "bold")
    else:
        bg_color = "SystemButtonFace"
        fg_color = "black"
        font = ("Arial", 10)
    
    button = tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        height=height,
        state=state,
        bg=bg_color,
        fg=fg_color,
        font=font
    )
    
    return button