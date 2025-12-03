# Exports all config settings so users can import from one place
from src.core.config.app_config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT
from src.core.config.chart_config import CHART_SETTINGS
from src.core.config.ui_config import COLORS
from src.core.config.messages import ERROR_MESSAGES, STATUS_MESSAGES

__all__ = ['APP_NAME', 'WINDOW_WIDTH', ...]  # Optional: explicit exports