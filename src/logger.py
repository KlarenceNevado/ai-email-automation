import logging
import os

# Configure logging to both file and console for professional observability
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def log_info(message):
    """Logs an informational message."""
    logging.info(message)

def log_error(message):
    """Logs an error message."""
    logging.error(message)
