import yaml
from udp_generator import UDPGeneratorSettings
class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config : dict = yaml.safe_load(open(config_path))

    def get_timing_config(self) -> dict:
        return self.config.get("timing", {})

    def get_payload_config(self) -> dict:
        return self.config.get("payload", {})

    def get_session_config(self) -> dict:
        return self.config.get("session", {})

    def get_output_config(self) -> dict:
        return self.config.get("output", {})

    def get_udp_generator_config(self) -> UDPGeneratorSettings:
        return UDPGeneratorSettings(
            target_ip=self.config.get("session", {}).get("host", "127.0.0.1"),
            target_port=self.config.get("session", {}).get("port", 5000),
            stop_after=self.config.get("session", {}).get("stop_after", {"mode": "forever"}),
            payload_settings=self.get_payload_config(),
            timing_settings=self.get_timing_config(),
            )