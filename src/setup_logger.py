import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s][%(levelname)s]%(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(stream_handler)