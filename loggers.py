import logging


def create_and_set_loggers():
    logger = logging.getLogger('basic')
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    logger.addHandler(console_handler)

