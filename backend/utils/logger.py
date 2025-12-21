import logging
from rich.logging import RichHandler

def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
        datefmt="[%X]",
        handlers=[RichHandler()]
    )

def get_logger(name: str):
    setup_logger()
    return logging.getLogger(name)
