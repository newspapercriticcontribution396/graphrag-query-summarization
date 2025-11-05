import logging
import sys
import os

def setup_logging():
    """Configures the root logger for console and file output."""
    
    # Ensure logs directory exists
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, "graph_rag.log")

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console handler
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)
    stdout_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    stdout_handler.setFormatter(stdout_formatter)
    logger.addHandler(stdout_handler)

    # File handler
    file_handler = logging.FileHandler(log_file_path, mode='a')
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    logging.info("Logging configured. Saving logs to %s", log_file_path)

    # Add uncaught exception hook
    def handle_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        logging.critical("Uncaught exception:", exc_info=(exc_type, exc_value, exc_traceback))

    sys.excepthook = handle_exception
