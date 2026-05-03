
from scapy.all import IP, UDP, Raw, send

from models.models import StopAfter
import time
import logging

logger = logging.getLogger(__name__)

class UDPGenerator:
    def __init__(self, target_ip, target_port):
        self.target_ip = target_ip
        self.target_port = target_port

    def _create_packet(self):
        return IP(dst=self.target_ip) / UDP(dport=self.target_port) / Raw(load=b"Test packet")

    def generate_udp_packets(self, stop_after: StopAfter=None):
        logger.info("Starting UDP packet generation to %s:%d with stop condition: %s", self.target_ip, self.target_port, stop_after)
        if stop_after is None:
            stop_after = StopAfter(mode="forever")

        if stop_after.get("mode") == "duration":
            end_time = time.time() + stop_after.get("seconds")
            while time.time() < end_time:
                send(self._create_packet())
        elif stop_after.get("mode") == "packet_count":
            for _ in range(stop_after.get("packets")):
                send(self._create_packet())
        elif stop_after.get("mode") == "bytes":
            bytes_sent = 0
            packet = self._create_packet()
            while bytes_sent < stop_after.get("megabytes") * 1024 * 1024:
                send(packet)
                bytes_sent += len(packet)
        elif stop_after.get("mode") == "forever":
            packet = self._create_packet()
            while True:
                send(packet)

        logger.info("Finished UDP packet generation to %s:%d", self.target_ip, self.target_port)
    