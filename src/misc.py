import os
import sys


def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, for PyInstaller."""
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)
