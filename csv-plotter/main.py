"""
CSV Plotter - Main Entry Point
Simple Python application to plot CSV data
"""
import tkinter as tk
from src.gui.main_window import MainWindow

def main():
    """Start the CSV Plotter application"""
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()