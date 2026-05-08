from dataclasses import dataclass
from typing import Literal

@dataclass
class StopAfter:
    mode: Literal["duration", "packet_count", "bytes", "forever"]
    seconds: int = None
    packets: int = None
    megabytes: int = None

@dataclass
class SessionConfig:
    host: str
    port: int
    bind_port: int
    stop_after: StopAfter

@dataclass
class PayloadSettings:
    size: int
    pattern: str

@dataclass
class TimingSettings:
    inter_packet_delay_ms: int