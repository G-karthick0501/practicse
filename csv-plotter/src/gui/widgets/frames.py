"""
Frame Components
Frame factory functions
"""
import tkinter as tk


def create_frame(parent, padding=10):
    """
    Factory method for creating frames
    
    Args:
        parent: Parent widget
        padding: Frame padding
    
    Returns:
        tk.Frame: Configured frame
    """
    frame = tk.Frame(parent, pady=padding)
    return frame