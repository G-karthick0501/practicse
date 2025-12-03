"""
Bar Chart
Creates bar charts
"""
import matplotlib.pyplot as plt
from src.core.config import CHART_SETTINGS, COLORS
from src.core.charts.chart_base import (
    create_chart_window, 
    embed_chart_in_window, 
    apply_common_styling
)


def create_bar_chart(df, x_column, y_column):
    """
    Create a bar chart in a new window
    
    Args:
        df: pandas DataFrame
        x_column: Column name for X-axis
        y_column: Column name for Y-axis
    
    Returns:
        chart_window: Toplevel window containing the chart
    """
    # Create window
    window = create_chart_window(f"Bar Chart: {y_column} vs {x_column}")
    
    # Create figure
    fig, ax = plt.subplots(
        figsize=(CHART_SETTINGS['figure_width'], CHART_SETTINGS['figure_height'])
    )
    
    # Plot bar chart
    ax.bar(
        df[x_column],
        df[y_column],
        color=COLORS['bar_chart'],
        alpha=CHART_SETTINGS['bar_alpha'],
        edgecolor=COLORS['bar_edge'],
        linewidth=CHART_SETTINGS['bar_edge_width']
    )
    
    # Add grid (y-axis only for bar charts)
    ax.grid(True, alpha=CHART_SETTINGS['grid_alpha'], linestyle='--', axis='y')
    
    # Apply common styling
    apply_common_styling(ax, x_column, y_column, f'{y_column} vs {x_column}')
    
    # Embed in window
    embed_chart_in_window(fig, window)
    
    return window