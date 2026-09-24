import psutil


def get_disk_usage(path="/"):
    """Return disk usage information for the given path."""

    usage = psutil.disk_usage(path)

    disk_info = {
        "total": usage.total,
        "used": usage.used,
        "free": usage.free,
        "percent": usage.percent,
    }

    return disk_info


def format_bytes(value):
    """Convert bytes into a readable GB value."""

    return f"{value / (1024 ** 3):.2f} GB"