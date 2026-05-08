
from scapy.all import IP, UDP, Raw, send

from models.models import PayloadSettings, StopAfter, TimingSettings
import time
import logging
from dataclasses import dataclass
logger = logging.getLogger(__name__)

@dataclass
class UDPGeneratorSettings:
    target_ip: str
    target_port: int
    stop_after: StopAfter
    payload_settings: PayloadSettings
    timing_settings: TimingSettings
class UDPGenerator:
    def __init__(self, settings: UDPGeneratorSettings):
        self.settings = settings


    def _create_packet(self):
        return IP(dst=self.settings.target_ip) / UDP(dport=self.settings.target_port) / Raw(load=b"Test packet")

    def generate_udp_packets(self):
        logger.info("Starting UDP packet generation to %s:%d with stop condition: %s", self.settings.target_ip, self.settings.target_port, self.settings.stop_after)
        if self.settings.stop_after is None:
            self.settings.stop_after = StopAfter(mode="forever")

        if self.settings.stop_after.get("mode") == "duration":
            end_time = time.time() + self.settings.stop_after.get("seconds")
            while time.time() < end_time:
                send(self._create_packet())
        elif self.settings.stop_after.get("mode") == "packet_count":
            for _ in range(self.settings.stop_after.get("packets")):
                send(self._create_packet())
        elif self.settings.stop_after.get("mode") == "bytes":
            bytes_sent = 0
            packet = self._create_packet()
            while bytes_sent < self.settings.stop_after.get("megabytes") * 1024 * 1024:
                send(packet)
                bytes_sent += len(packet)
        elif self.settings.stop_after.get("mode") == "forever":
            packet = self._create_packet()
            while True:
                send(packet)

        logger.info("Finished UDP packet generation to %s:%d", self.settings.target_ip, self.settings.target_port)
    