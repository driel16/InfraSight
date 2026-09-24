import os
import platform
from pathlib import Path


def get_system_info():
    """Collect basic information about the current system."""

    system_info = {
        "operating_system": platform.system(),
        "hostname": platform.node(),
        "python_version": platform.python_version(),
        "architecture": platform.machine(),
        "kernel": platform.release(),
        "current_user": os.environ.get("USER", "Unknown"),
        "home_directory": str(Path.home()),
        "working_directory": str(Path.cwd()),
    }

    return system_info