import logging
from logging import StreamHandler, Formatter
import os


def configure_logging():
    level_name = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    level = getattr(logging, level_name, logging.DEBUG)
    handler = StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s [%(name)s] %(message)s'))
    root = logging.getLogger()
    root.setLevel(level)
    # avoid adding multiple handlers in case of re-imports
    if not any(isinstance(h, StreamHandler) for h in root.handlers):
        root.addHandler(handler)
