import yaml

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = yaml.safe_load(open(config_path))

    def get_timing_config(self) -> dict:
        return self.config.get("timing", {})

    def get_payload_config(self) -> dict:
        return self.config.get("payload", {})

    def get_session_config(self) -> dict:
        return self.config.get("session", {})

    def get_output_config(self) -> dict:
        return self.config.get("output", {})