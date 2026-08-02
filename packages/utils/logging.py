import logging

def init_logger(name: str) -> logging.Logger:
  logger = logging.getLogger(name)
  logger.setLevel(logging.INFO)
  return logger