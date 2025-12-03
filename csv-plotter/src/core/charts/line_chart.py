"""
Line Chart
Creates line charts
"""
import matplotlib.pyplot as plt
from src.core.config import CHART_SETTINGS, COLORS
from src.core.charts.chart_base import (
    create_chart_window, 
    embed_chart_in_window, 
    apply_common_styling
)


def create_line_chart(df, x_column, y_column):
    """
    Create a line chart in a new window
    
    Args:
        df: pandas DataFrame
        x_column: Column name for X-axis
        y_column: Column name for Y-axis
    
    Returns:
        chart_window: Toplevel window containing the chart
    """
    # Create window
    window = create_chart_window(f"Line Chart: {y_column} vs {x_column}")
    
    # Create figure
    fig, ax = plt.subplots(
        figsize=(CHART_SETTINGS['figure_width'], CHART_SETTINGS['figure_height'])
    )
    
    # Plot line chart
    ax.plot(
        df[x_column],
        df[y_column],
        color=COLORS['line_chart'],
        linewidth=CHART_SETTINGS['line_width'],
        marker='o',
        markersize=CHART_SETTINGS['marker_size']
    )
    
    # Add grid
    ax.grid(True, alpha=CHART_SETTINGS['grid_alpha'], linestyle='--')
    
    # Apply common styling
    apply_common_styling(ax, x_column, y_column, f'{y_column} vs {x_column}')
    
    # Embed in window with save functionality
    chart_name = f"line_chart_{y_column}_vs_{x_column}"
    embed_chart_in_window(fig, window, chart_name)
    
    return window