"""
Status Bar
Handles status messages and user feedback
Follows Single Responsibility Principle
"""
import tkinter as tk
from src.core.config import COLORS 


class StatusBar:
    """
    Status bar for displaying application status messages
    Decoupled component that can be reused
    """
    
    def __init__(self, parent):
        """
        Initialize status bar
        
        Args:
            parent: Parent widget
        """
        self.frame = tk.Frame(parent, relief=tk.SUNKEN, bd=1)
        self.frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.label = tk.Label(
            self.frame,
            text="Ready",
            anchor=tk.W,
            padx=10,
            pady=5,
            font=("Arial", 9)
        )
        self.label.pack(fill=tk.X)
        
        self.default_text = "Ready"
    
    def set_message(self, message, message_type="info"):
        """
        Display a status message
        
        Args:
            message: Message text
            message_type: Type of message ('info', 'success', 'error', 'warning')
        """
        # Set color based on message type
        color_map = {
            "info": "black",
            "success": COLORS['success'],
            "error": COLORS['error'],
            "warning": COLORS['warning']
        }
        
        color = color_map.get(message_type, "black")
        
        self.label.config(text=message, fg=color)
        
        # Auto-clear error and warning messages after 5 seconds
        if message_type in ["error", "warning"]:
            self.label.after(5000, self.clear)
    
    def set_success(self, message):
        """Shortcut for success message"""
        self.set_message(message, "success")
    
    def set_error(self, message):
        """Shortcut for error message"""
        self.set_message(message, "error")
    
    def set_info(self, message):
        """Shortcut for info message"""
        self.set_message(message, "info")
    
    def set_warning(self, message):
        """Shortcut for warning message"""
        self.set_message(message, "warning")
    
    def clear(self):
        """Clear status message and show default"""
        self.label.config(text=self.default_text, fg="black")