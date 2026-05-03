import logging

from udp_generator import UDPGenerator
logger = logging.getLogger(__name__)

class SessionHandler:
    def __init__(self, session_config, udp_generator: UDPGenerator):
        self.session_config = session_config
        self.udp_generator = udp_generator

    def start_session(self):
        try:
            logger.info("Starting session with config: %s", self.session_config)
            self.udp_generator.generate_udp_packets(stop_after=self.session_config.get("stop_after"))
            logger.info("Session completed")
        
        except Exception as e:
            logger.error("Error during session: %s", e)