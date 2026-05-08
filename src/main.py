
import os

from config_loader import ConfigLoader
from session_handler import SessionHandler
from udp_generator import UDPGenerator
from setup_logger import setup_logger
from pathlib import Path

if __name__ == "__main__":
    setup_logger()
    config_loader = ConfigLoader(Path("config") / "config.yaml")

    target_ip = "127.0.0.1"
    target_port = 5000

    session_handler = SessionHandler(config_loader.get_session_config(), UDPGenerator(config_loader.get_udp_generator_config()))
    session_handler.start_session()