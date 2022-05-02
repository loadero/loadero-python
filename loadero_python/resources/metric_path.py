"""Loadero metric path constants."""

from __future__ import annotations
from enum import Enum
from loadero_python.resources.resource import LoaderoResource

# This file is generated automatically by generate-constants/generate.py script.


class MetricPath(LoaderoResource, Enum):
    """MetricPath enumerates Loadero metric path constants."""

    MACHINE_CPU_AVAILABLE_TOTAL = "machine/cpu/available/total"

    MACHINE_CPU_PERCENT_25TH = "machine/cpu/percent/25th"

    MACHINE_CPU_PERCENT_50TH = "machine/cpu/percent/50th"

    MACHINE_CPU_PERCENT_75TH = "machine/cpu/percent/75th"

    MACHINE_CPU_PERCENT_95TH = "machine/cpu/percent/95th"

    MACHINE_CPU_PERCENT_99TH = "machine/cpu/percent/99th"

    MACHINE_CPU_PERCENT_AVG = "machine/cpu/percent/avg"

    MACHINE_CPU_PERCENT_MAX = "machine/cpu/percent/max"

    MACHINE_CPU_PERCENT_STDDEV = "machine/cpu/percent/stddev"

    MACHINE_CPU_USED_25TH = "machine/cpu/used/25th"

    MACHINE_CPU_USED_50TH = "machine/cpu/used/50th"

    MACHINE_CPU_USED_75TH = "machine/cpu/used/75th"

    MACHINE_CPU_USED_95TH = "machine/cpu/used/95th"

    MACHINE_CPU_USED_99TH = "machine/cpu/used/99th"

    MACHINE_CPU_USED_AVG = "machine/cpu/used/avg"

    MACHINE_CPU_USED_MAX = "machine/cpu/used/max"

    MACHINE_CPU_USED_RSTDDEV = "machine/cpu/used/rstddev"

    MACHINE_CPU_USED_STDDEV = "machine/cpu/used/stddev"

    MACHINE_NETWORK_BITRATE_IN_25TH = "machine/network/bitrate/in/25th"

    MACHINE_NETWORK_BITRATE_IN_50TH = "machine/network/bitrate/in/50th"

    MACHINE_NETWORK_BITRATE_IN_75TH = "machine/network/bitrate/in/75th"

    MACHINE_NETWORK_BITRATE_IN_95TH = "machine/network/bitrate/in/95th"

    MACHINE_NETWORK_BITRATE_IN_99TH = "machine/network/bitrate/in/99th"

    MACHINE_NETWORK_BITRATE_IN_AVG = "machine/network/bitrate/in/avg"

    MACHINE_NETWORK_BITRATE_IN_MAX = "machine/network/bitrate/in/max"

    MACHINE_NETWORK_BITRATE_IN_MIN = "machine/network/bitrate/in/min"

    MACHINE_NETWORK_BITRATE_IN_RSTDDEV = "machine/network/bitrate/in/rstddev"

    MACHINE_NETWORK_BITRATE_IN_STDDEV = "machine/network/bitrate/in/stddev"

    MACHINE_NETWORK_BITRATE_OUT_25TH = "machine/network/bitrate/out/25th"

    MACHINE_NETWORK_BITRATE_OUT_50TH = "machine/network/bitrate/out/50th"

    MACHINE_NETWORK_BITRATE_OUT_75TH = "machine/network/bitrate/out/75th"

    MACHINE_NETWORK_BITRATE_OUT_95TH = "machine/network/bitrate/out/95th"

    MACHINE_NETWORK_BITRATE_OUT_99TH = "machine/network/bitrate/out/99th"

    MACHINE_NETWORK_BITRATE_OUT_AVG = "machine/network/bitrate/out/avg"

    MACHINE_NETWORK_BITRATE_OUT_MAX = "machine/network/bitrate/out/max"

    MACHINE_NETWORK_BITRATE_OUT_MIN = "machine/network/bitrate/out/min"

    MACHINE_NETWORK_BITRATE_OUT_RSTDDEV = "machine/network/bitrate/out/rstddev"

    MACHINE_NETWORK_BITRATE_OUT_STDDEV = "machine/network/bitrate/out/stddev"

    MACHINE_NETWORK_BYTES_IN_TOTAL = "machine/network/bytes/in/total"

    MACHINE_NETWORK_BYTES_OUT_TOTAL = "machine/network/bytes/out/total"

    MACHINE_NETWORK_ERRORS_IN_TOTAL = "machine/network/errors/in/total"

    MACHINE_NETWORK_ERRORS_OUT_TOTAL = "machine/network/errors/out/total"

    MACHINE_NETWORK_PACKETSLOST_IN_PERCENT = (
        "machine/network/packetsLost/in/percent"
    )

    MACHINE_NETWORK_PACKETSLOST_OUT_PERCENT = (
        "machine/network/packetsLost/out/percent"
    )

    MACHINE_NETWORK_PACKETS_IN_25TH = "machine/network/packets/in/25th"

    MACHINE_NETWORK_PACKETS_IN_50TH = "machine/network/packets/in/50th"

    MACHINE_NETWORK_PACKETS_IN_75TH = "machine/network/packets/in/75th"

    MACHINE_NETWORK_PACKETS_IN_95TH = "machine/network/packets/in/95th"

    MACHINE_NETWORK_PACKETS_IN_99TH = "machine/network/packets/in/99th"

    MACHINE_NETWORK_PACKETS_IN_AVG = "machine/network/packets/in/avg"

    MACHINE_NETWORK_PACKETS_IN_MAX = "machine/network/packets/in/max"

    MACHINE_NETWORK_PACKETS_IN_RSTDDEV = "machine/network/packets/in/rstddev"

    MACHINE_NETWORK_PACKETS_IN_STDDEV = "machine/network/packets/in/stddev"

    MACHINE_NETWORK_PACKETS_IN_TOTAL = "machine/network/packets/in/total"

    MACHINE_NETWORK_PACKETS_OUT_25TH = "machine/network/packets/out/25th"

    MACHINE_NETWORK_PACKETS_OUT_50TH = "machine/network/packets/out/50th"

    MACHINE_NETWORK_PACKETS_OUT_75TH = "machine/network/packets/out/75th"

    MACHINE_NETWORK_PACKETS_OUT_95TH = "machine/network/packets/out/95th"

    MACHINE_NETWORK_PACKETS_OUT_99TH = "machine/network/packets/out/99th"

    MACHINE_NETWORK_PACKETS_OUT_AVG = "machine/network/packets/out/avg"

    MACHINE_NETWORK_PACKETS_OUT_MAX = "machine/network/packets/out/max"

    MACHINE_NETWORK_PACKETS_OUT_RSTDDEV = "machine/network/packets/out/rstddev"

    MACHINE_NETWORK_PACKETS_OUT_STDDEV = "machine/network/packets/out/stddev"

    MACHINE_NETWORK_PACKETS_OUT_TOTAL = "machine/network/packets/out/total"

    MACHINE_RAM_AVAILABLE_TOTAL = "machine/ram/available/total"

    MACHINE_RAM_PERCENT_25TH = "machine/ram/percent/25th"

    MACHINE_RAM_PERCENT_50TH = "machine/ram/percent/50th"

    MACHINE_RAM_PERCENT_75TH = "machine/ram/percent/75th"

    MACHINE_RAM_PERCENT_95TH = "machine/ram/percent/95th"

    MACHINE_RAM_PERCENT_99TH = "machine/ram/percent/99th"

    MACHINE_RAM_PERCENT_AVG = "machine/ram/percent/avg"

    MACHINE_RAM_PERCENT_MAX = "machine/ram/percent/max"

    MACHINE_RAM_PERCENT_STDDEV = "machine/ram/percent/stddev"

    MACHINE_RAM_USED_25TH = "machine/ram/used/25th"

    MACHINE_RAM_USED_50TH = "machine/ram/used/50th"

    MACHINE_RAM_USED_75TH = "machine/ram/used/75th"

    MACHINE_RAM_USED_95TH = "machine/ram/used/95th"

    MACHINE_RAM_USED_99TH = "machine/ram/used/99th"

    MACHINE_RAM_USED_AVG = "machine/ram/used/avg"

    MACHINE_RAM_USED_MAX = "machine/ram/used/max"

    MACHINE_RAM_USED_RSTDDEV = "machine/ram/used/rstddev"

    MACHINE_RAM_USED_STDDEV = "machine/ram/used/stddev"

    WEBRTC_AUDIO_BITRATE_IN_25TH = "webrtc/audio/bitrate/in/25th"

    WEBRTC_AUDIO_BITRATE_IN_50TH = "webrtc/audio/bitrate/in/50th"

    WEBRTC_AUDIO_BITRATE_IN_75TH = "webrtc/audio/bitrate/in/75th"

    WEBRTC_AUDIO_BITRATE_IN_95TH = "webrtc/audio/bitrate/in/95th"

    WEBRTC_AUDIO_BITRATE_IN_99TH = "webrtc/audio/bitrate/in/99th"

    WEBRTC_AUDIO_BITRATE_IN_AVG = "webrtc/audio/bitrate/in/avg"

    WEBRTC_AUDIO_BITRATE_IN_MAX = "webrtc/audio/bitrate/in/max"

    WEBRTC_AUDIO_BITRATE_IN_MIN = "webrtc/audio/bitrate/in/min"

    WEBRTC_AUDIO_BITRATE_IN_RSTDDEV = "webrtc/audio/bitrate/in/rstddev"

    WEBRTC_AUDIO_BITRATE_IN_STDDEV = "webrtc/audio/bitrate/in/stddev"

    WEBRTC_AUDIO_BITRATE_OUT_25TH = "webrtc/audio/bitrate/out/25th"

    WEBRTC_AUDIO_BITRATE_OUT_50TH = "webrtc/audio/bitrate/out/50th"

    WEBRTC_AUDIO_BITRATE_OUT_75TH = "webrtc/audio/bitrate/out/75th"

    WEBRTC_AUDIO_BITRATE_OUT_95TH = "webrtc/audio/bitrate/out/95th"

    WEBRTC_AUDIO_BITRATE_OUT_99TH = "webrtc/audio/bitrate/out/99th"

    WEBRTC_AUDIO_BITRATE_OUT_AVG = "webrtc/audio/bitrate/out/avg"

    WEBRTC_AUDIO_BITRATE_OUT_MAX = "webrtc/audio/bitrate/out/max"

    WEBRTC_AUDIO_BITRATE_OUT_MIN = "webrtc/audio/bitrate/out/min"

    WEBRTC_AUDIO_BITRATE_OUT_RSTDDEV = "webrtc/audio/bitrate/out/rstddev"

    WEBRTC_AUDIO_BITRATE_OUT_STDDEV = "webrtc/audio/bitrate/out/stddev"

    WEBRTC_AUDIO_BYTES_IN_TOTAL = "webrtc/audio/bytes/in/total"

    WEBRTC_AUDIO_BYTES_OUT_TOTAL = "webrtc/audio/bytes/out/total"

    WEBRTC_AUDIO_CODEC_IN = "webrtc/audio/codec/in"

    WEBRTC_AUDIO_CODEC_OUT = "webrtc/audio/codec/out"

    WEBRTC_AUDIO_CONNECTIONS_IN = "webrtc/audio/connections/in"

    WEBRTC_AUDIO_CONNECTIONS_OUT = "webrtc/audio/connections/out"

    WEBRTC_AUDIO_JITTERBUFFER_25TH = "webrtc/audio/jitterBuffer/25th"

    WEBRTC_AUDIO_JITTERBUFFER_50TH = "webrtc/audio/jitterBuffer/50th"

    WEBRTC_AUDIO_JITTERBUFFER_75TH = "webrtc/audio/jitterBuffer/75th"

    WEBRTC_AUDIO_JITTERBUFFER_95TH = "webrtc/audio/jitterBuffer/95th"

    WEBRTC_AUDIO_JITTERBUFFER_99TH = "webrtc/audio/jitterBuffer/99th"

    WEBRTC_AUDIO_JITTERBUFFER_AVG = "webrtc/audio/jitterBuffer/avg"

    WEBRTC_AUDIO_JITTERBUFFER_MAX = "webrtc/audio/jitterBuffer/max"

    WEBRTC_AUDIO_JITTERBUFFER_RSTDDEV = "webrtc/audio/jitterBuffer/rstddev"

    WEBRTC_AUDIO_JITTERBUFFER_STDDEV = "webrtc/audio/jitterBuffer/stddev"

    WEBRTC_AUDIO_JITTER_IN_25TH = "webrtc/audio/jitter/in/25th"

    WEBRTC_AUDIO_JITTER_IN_50TH = "webrtc/audio/jitter/in/50th"

    WEBRTC_AUDIO_JITTER_IN_75TH = "webrtc/audio/jitter/in/75th"

    WEBRTC_AUDIO_JITTER_IN_95TH = "webrtc/audio/jitter/in/95th"

    WEBRTC_AUDIO_JITTER_IN_99TH = "webrtc/audio/jitter/in/99th"

    WEBRTC_AUDIO_JITTER_IN_AVG = "webrtc/audio/jitter/in/avg"

    WEBRTC_AUDIO_JITTER_IN_MAX = "webrtc/audio/jitter/in/max"

    WEBRTC_AUDIO_JITTER_IN_RSTDDEV = "webrtc/audio/jitter/in/rstddev"

    WEBRTC_AUDIO_JITTER_IN_STDDEV = "webrtc/audio/jitter/in/stddev"

    WEBRTC_AUDIO_JITTER_OUT_25TH = "webrtc/audio/jitter/out/25th"

    WEBRTC_AUDIO_JITTER_OUT_50TH = "webrtc/audio/jitter/out/50th"

    WEBRTC_AUDIO_JITTER_OUT_75TH = "webrtc/audio/jitter/out/75th"

    WEBRTC_AUDIO_JITTER_OUT_95TH = "webrtc/audio/jitter/out/95th"

    WEBRTC_AUDIO_JITTER_OUT_99TH = "webrtc/audio/jitter/out/99th"

    WEBRTC_AUDIO_JITTER_OUT_AVG = "webrtc/audio/jitter/out/avg"

    WEBRTC_AUDIO_JITTER_OUT_MAX = "webrtc/audio/jitter/out/max"

    WEBRTC_AUDIO_JITTER_OUT_RSTDDEV = "webrtc/audio/jitter/out/rstddev"

    WEBRTC_AUDIO_JITTER_OUT_STDDEV = "webrtc/audio/jitter/out/stddev"

    WEBRTC_AUDIO_LEVEL_IN_25TH = "webrtc/audio/level/in/25th"

    WEBRTC_AUDIO_LEVEL_IN_50TH = "webrtc/audio/level/in/50th"

    WEBRTC_AUDIO_LEVEL_IN_75TH = "webrtc/audio/level/in/75th"

    WEBRTC_AUDIO_LEVEL_IN_95TH = "webrtc/audio/level/in/95th"

    WEBRTC_AUDIO_LEVEL_IN_99TH = "webrtc/audio/level/in/99th"

    WEBRTC_AUDIO_LEVEL_IN_AVG = "webrtc/audio/level/in/avg"

    WEBRTC_AUDIO_LEVEL_IN_MAX = "webrtc/audio/level/in/max"

    WEBRTC_AUDIO_LEVEL_IN_RSTDDEV = "webrtc/audio/level/in/rstddev"

    WEBRTC_AUDIO_LEVEL_IN_STDDEV = "webrtc/audio/level/in/stddev"

    WEBRTC_AUDIO_LEVEL_OUT_25TH = "webrtc/audio/level/out/25th"

    WEBRTC_AUDIO_LEVEL_OUT_50TH = "webrtc/audio/level/out/50th"

    WEBRTC_AUDIO_LEVEL_OUT_75TH = "webrtc/audio/level/out/75th"

    WEBRTC_AUDIO_LEVEL_OUT_95TH = "webrtc/audio/level/out/95th"

    WEBRTC_AUDIO_LEVEL_OUT_99TH = "webrtc/audio/level/out/99th"

    WEBRTC_AUDIO_LEVEL_OUT_AVG = "webrtc/audio/level/out/avg"

    WEBRTC_AUDIO_LEVEL_OUT_MAX = "webrtc/audio/level/out/max"

    WEBRTC_AUDIO_LEVEL_OUT_RSTDDEV = "webrtc/audio/level/out/rstddev"

    WEBRTC_AUDIO_LEVEL_OUT_STDDEV = "webrtc/audio/level/out/stddev"

    WEBRTC_AUDIO_PACKETSLOST_IN_PERCENT = "webrtc/audio/packetsLost/in/percent"

    WEBRTC_AUDIO_PACKETSLOST_IN_TOTAL = "webrtc/audio/packetsLost/in/total"

    WEBRTC_AUDIO_PACKETSLOST_OUT_PERCENT = (
        "webrtc/audio/packetsLost/out/percent"
    )

    WEBRTC_AUDIO_PACKETSLOST_OUT_TOTAL = "webrtc/audio/packetsLost/out/total"

    WEBRTC_AUDIO_PACKETS_IN_25TH = "webrtc/audio/packets/in/25th"

    WEBRTC_AUDIO_PACKETS_IN_50TH = "webrtc/audio/packets/in/50th"

    WEBRTC_AUDIO_PACKETS_IN_75TH = "webrtc/audio/packets/in/75th"

    WEBRTC_AUDIO_PACKETS_IN_95TH = "webrtc/audio/packets/in/95th"

    WEBRTC_AUDIO_PACKETS_IN_99TH = "webrtc/audio/packets/in/99th"

    WEBRTC_AUDIO_PACKETS_IN_AVG = "webrtc/audio/packets/in/avg"

    WEBRTC_AUDIO_PACKETS_IN_MAX = "webrtc/audio/packets/in/max"

    WEBRTC_AUDIO_PACKETS_IN_RSTDDEV = "webrtc/audio/packets/in/rstddev"

    WEBRTC_AUDIO_PACKETS_IN_STDDEV = "webrtc/audio/packets/in/stddev"

    WEBRTC_AUDIO_PACKETS_IN_TOTAL = "webrtc/audio/packets/in/total"

    WEBRTC_AUDIO_PACKETS_OUT_25TH = "webrtc/audio/packets/out/25th"

    WEBRTC_AUDIO_PACKETS_OUT_50TH = "webrtc/audio/packets/out/50th"

    WEBRTC_AUDIO_PACKETS_OUT_75TH = "webrtc/audio/packets/out/75th"

    WEBRTC_AUDIO_PACKETS_OUT_95TH = "webrtc/audio/packets/out/95th"

    WEBRTC_AUDIO_PACKETS_OUT_99TH = "webrtc/audio/packets/out/99th"

    WEBRTC_AUDIO_PACKETS_OUT_AVG = "webrtc/audio/packets/out/avg"

    WEBRTC_AUDIO_PACKETS_OUT_MAX = "webrtc/audio/packets/out/max"

    WEBRTC_AUDIO_PACKETS_OUT_RSTDDEV = "webrtc/audio/packets/out/rstddev"

    WEBRTC_AUDIO_PACKETS_OUT_STDDEV = "webrtc/audio/packets/out/stddev"

    WEBRTC_AUDIO_PACKETS_OUT_TOTAL = "webrtc/audio/packets/out/total"

    WEBRTC_AUDIO_RTT_25TH = "webrtc/audio/rtt/25th"

    WEBRTC_AUDIO_RTT_50TH = "webrtc/audio/rtt/50th"

    WEBRTC_AUDIO_RTT_75TH = "webrtc/audio/rtt/75th"

    WEBRTC_AUDIO_RTT_95TH = "webrtc/audio/rtt/95th"

    WEBRTC_AUDIO_RTT_99TH = "webrtc/audio/rtt/99th"

    WEBRTC_AUDIO_RTT_AVG = "webrtc/audio/rtt/avg"

    WEBRTC_AUDIO_RTT_MAX = "webrtc/audio/rtt/max"

    WEBRTC_AUDIO_RTT_RSTDDEV = "webrtc/audio/rtt/rstddev"

    WEBRTC_AUDIO_RTT_STDDEV = "webrtc/audio/rtt/stddev"

    WEBRTC_VIDEO_BITRATE_IN_25TH = "webrtc/video/bitrate/in/25th"

    WEBRTC_VIDEO_BITRATE_IN_50TH = "webrtc/video/bitrate/in/50th"

    WEBRTC_VIDEO_BITRATE_IN_75TH = "webrtc/video/bitrate/in/75th"

    WEBRTC_VIDEO_BITRATE_IN_95TH = "webrtc/video/bitrate/in/95th"

    WEBRTC_VIDEO_BITRATE_IN_99TH = "webrtc/video/bitrate/in/99th"

    WEBRTC_VIDEO_BITRATE_IN_AVG = "webrtc/video/bitrate/in/avg"

    WEBRTC_VIDEO_BITRATE_IN_MAX = "webrtc/video/bitrate/in/max"

    WEBRTC_VIDEO_BITRATE_IN_MIN = "webrtc/video/bitrate/in/min"

    WEBRTC_VIDEO_BITRATE_IN_RSTDDEV = "webrtc/video/bitrate/in/rstddev"

    WEBRTC_VIDEO_BITRATE_IN_STDDEV = "webrtc/video/bitrate/in/stddev"

    WEBRTC_VIDEO_BITRATE_OUT_25TH = "webrtc/video/bitrate/out/25th"

    WEBRTC_VIDEO_BITRATE_OUT_50TH = "webrtc/video/bitrate/out/50th"

    WEBRTC_VIDEO_BITRATE_OUT_75TH = "webrtc/video/bitrate/out/75th"

    WEBRTC_VIDEO_BITRATE_OUT_95TH = "webrtc/video/bitrate/out/95th"

    WEBRTC_VIDEO_BITRATE_OUT_99TH = "webrtc/video/bitrate/out/99th"

    WEBRTC_VIDEO_BITRATE_OUT_AVG = "webrtc/video/bitrate/out/avg"

    WEBRTC_VIDEO_BITRATE_OUT_MAX = "webrtc/video/bitrate/out/max"

    WEBRTC_VIDEO_BITRATE_OUT_MIN = "webrtc/video/bitrate/out/min"

    WEBRTC_VIDEO_BITRATE_OUT_RSTDDEV = "webrtc/video/bitrate/out/rstddev"

    WEBRTC_VIDEO_BITRATE_OUT_STDDEV = "webrtc/video/bitrate/out/stddev"

    WEBRTC_VIDEO_BYTES_IN_TOTAL = "webrtc/video/bytes/in/total"

    WEBRTC_VIDEO_BYTES_OUT_TOTAL = "webrtc/video/bytes/out/total"

    WEBRTC_VIDEO_CODEC_IN = "webrtc/video/codec/in"

    WEBRTC_VIDEO_CODEC_OUT = "webrtc/video/codec/out"

    WEBRTC_VIDEO_CONNECTIONS_IN = "webrtc/video/connections/in"

    WEBRTC_VIDEO_CONNECTIONS_OUT = "webrtc/video/connections/out"

    WEBRTC_VIDEO_FPS_IN_25TH = "webrtc/video/fps/in/25th"

    WEBRTC_VIDEO_FPS_IN_50TH = "webrtc/video/fps/in/50th"

    WEBRTC_VIDEO_FPS_IN_75TH = "webrtc/video/fps/in/75th"

    WEBRTC_VIDEO_FPS_IN_95TH = "webrtc/video/fps/in/95th"

    WEBRTC_VIDEO_FPS_IN_99TH = "webrtc/video/fps/in/99th"

    WEBRTC_VIDEO_FPS_IN_AVG = "webrtc/video/fps/in/avg"

    WEBRTC_VIDEO_FPS_IN_MAX = "webrtc/video/fps/in/max"

    WEBRTC_VIDEO_FPS_IN_RSTDDEV = "webrtc/video/fps/in/rstddev"

    WEBRTC_VIDEO_FPS_IN_STDDEV = "webrtc/video/fps/in/stddev"

    WEBRTC_VIDEO_FPS_OUT_25TH = "webrtc/video/fps/out/25th"

    WEBRTC_VIDEO_FPS_OUT_50TH = "webrtc/video/fps/out/50th"

    WEBRTC_VIDEO_FPS_OUT_75TH = "webrtc/video/fps/out/75th"

    WEBRTC_VIDEO_FPS_OUT_95TH = "webrtc/video/fps/out/95th"

    WEBRTC_VIDEO_FPS_OUT_99TH = "webrtc/video/fps/out/99th"

    WEBRTC_VIDEO_FPS_OUT_AVG = "webrtc/video/fps/out/avg"

    WEBRTC_VIDEO_FPS_OUT_MAX = "webrtc/video/fps/out/max"

    WEBRTC_VIDEO_FPS_OUT_RSTDDEV = "webrtc/video/fps/out/rstddev"

    WEBRTC_VIDEO_FPS_OUT_STDDEV = "webrtc/video/fps/out/stddev"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_25TH = "webrtc/video/frameHeight/in/25th"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_50TH = "webrtc/video/frameHeight/in/50th"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_75TH = "webrtc/video/frameHeight/in/75th"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_95TH = "webrtc/video/frameHeight/in/95th"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_99TH = "webrtc/video/frameHeight/in/99th"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_AVG = "webrtc/video/frameHeight/in/avg"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_MAX = "webrtc/video/frameHeight/in/max"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_MIN = "webrtc/video/frameHeight/in/min"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_RSTDDEV = "webrtc/video/frameHeight/in/rstddev"

    WEBRTC_VIDEO_FRAMEHEIGHT_IN_STDDEV = "webrtc/video/frameHeight/in/stddev"

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_25TH = "webrtc/video/frameHeight/out/25th"

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_50TH = "webrtc/video/frameHeight/out/50th"

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_75TH = "webrtc/video/frameHeight/out/75th"

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_95TH = "webrtc/video/frameHeight/out/95th"

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_99TH = "webrtc/video/frameHeight/out/99th"

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_AVG = "webrtc/video/frameHeight/out/avg"

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_MAX = "webrtc/video/frameHeight/out/max"

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_MIN = "webrtc/video/frameHeight/out/min"

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_RSTDDEV = (
        "webrtc/video/frameHeight/out/rstddev"
    )

    WEBRTC_VIDEO_FRAMEHEIGHT_OUT_STDDEV = "webrtc/video/frameHeight/out/stddev"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_25TH = "webrtc/video/frameWidth/in/25th"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_50TH = "webrtc/video/frameWidth/in/50th"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_75TH = "webrtc/video/frameWidth/in/75th"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_95TH = "webrtc/video/frameWidth/in/95th"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_99TH = "webrtc/video/frameWidth/in/99th"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_AVG = "webrtc/video/frameWidth/in/avg"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_MAX = "webrtc/video/frameWidth/in/max"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_MIN = "webrtc/video/frameWidth/in/min"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_RSTDDEV = "webrtc/video/frameWidth/in/rstddev"

    WEBRTC_VIDEO_FRAMEWIDTH_IN_STDDEV = "webrtc/video/frameWidth/in/stddev"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_25TH = "webrtc/video/frameWidth/out/25th"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_50TH = "webrtc/video/frameWidth/out/50th"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_75TH = "webrtc/video/frameWidth/out/75th"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_95TH = "webrtc/video/frameWidth/out/95th"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_99TH = "webrtc/video/frameWidth/out/99th"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_AVG = "webrtc/video/frameWidth/out/avg"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_MAX = "webrtc/video/frameWidth/out/max"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_MIN = "webrtc/video/frameWidth/out/min"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_RSTDDEV = "webrtc/video/frameWidth/out/rstddev"

    WEBRTC_VIDEO_FRAMEWIDTH_OUT_STDDEV = "webrtc/video/frameWidth/out/stddev"

    WEBRTC_VIDEO_JITTERBUFFER_25TH = "webrtc/video/jitterBuffer/25th"

    WEBRTC_VIDEO_JITTERBUFFER_50TH = "webrtc/video/jitterBuffer/50th"

    WEBRTC_VIDEO_JITTERBUFFER_75TH = "webrtc/video/jitterBuffer/75th"

    WEBRTC_VIDEO_JITTERBUFFER_95TH = "webrtc/video/jitterBuffer/95th"

    WEBRTC_VIDEO_JITTERBUFFER_99TH = "webrtc/video/jitterBuffer/99th"

    WEBRTC_VIDEO_JITTERBUFFER_AVG = "webrtc/video/jitterBuffer/avg"

    WEBRTC_VIDEO_JITTERBUFFER_MAX = "webrtc/video/jitterBuffer/max"

    WEBRTC_VIDEO_JITTERBUFFER_RSTDDEV = "webrtc/video/jitterBuffer/rstddev"

    WEBRTC_VIDEO_JITTERBUFFER_STDDEV = "webrtc/video/jitterBuffer/stddev"

    WEBRTC_VIDEO_JITTER_IN_25TH = "webrtc/video/jitter/in/25th"

    WEBRTC_VIDEO_JITTER_IN_50TH = "webrtc/video/jitter/in/50th"

    WEBRTC_VIDEO_JITTER_IN_75TH = "webrtc/video/jitter/in/75th"

    WEBRTC_VIDEO_JITTER_IN_95TH = "webrtc/video/jitter/in/95th"

    WEBRTC_VIDEO_JITTER_IN_99TH = "webrtc/video/jitter/in/99th"

    WEBRTC_VIDEO_JITTER_IN_AVG = "webrtc/video/jitter/in/avg"

    WEBRTC_VIDEO_JITTER_IN_MAX = "webrtc/video/jitter/in/max"

    WEBRTC_VIDEO_JITTER_IN_RSTDDEV = "webrtc/video/jitter/in/rstddev"

    WEBRTC_VIDEO_JITTER_IN_STDDEV = "webrtc/video/jitter/in/stddev"

    WEBRTC_VIDEO_JITTER_OUT_25TH = "webrtc/video/jitter/out/25th"

    WEBRTC_VIDEO_JITTER_OUT_50TH = "webrtc/video/jitter/out/50th"

    WEBRTC_VIDEO_JITTER_OUT_75TH = "webrtc/video/jitter/out/75th"

    WEBRTC_VIDEO_JITTER_OUT_95TH = "webrtc/video/jitter/out/95th"

    WEBRTC_VIDEO_JITTER_OUT_99TH = "webrtc/video/jitter/out/99th"

    WEBRTC_VIDEO_JITTER_OUT_AVG = "webrtc/video/jitter/out/avg"

    WEBRTC_VIDEO_JITTER_OUT_MAX = "webrtc/video/jitter/out/max"

    WEBRTC_VIDEO_JITTER_OUT_RSTDDEV = "webrtc/video/jitter/out/rstddev"

    WEBRTC_VIDEO_JITTER_OUT_STDDEV = "webrtc/video/jitter/out/stddev"

    WEBRTC_VIDEO_PACKETSLOST_IN_PERCENT = "webrtc/video/packetsLost/in/percent"

    WEBRTC_VIDEO_PACKETSLOST_IN_TOTAL = "webrtc/video/packetsLost/in/total"

    WEBRTC_VIDEO_PACKETSLOST_OUT_PERCENT = (
        "webrtc/video/packetsLost/out/percent"
    )

    WEBRTC_VIDEO_PACKETSLOST_OUT_TOTAL = "webrtc/video/packetsLost/out/total"

    WEBRTC_VIDEO_PACKETS_IN_25TH = "webrtc/video/packets/in/25th"

    WEBRTC_VIDEO_PACKETS_IN_50TH = "webrtc/video/packets/in/50th"

    WEBRTC_VIDEO_PACKETS_IN_75TH = "webrtc/video/packets/in/75th"

    WEBRTC_VIDEO_PACKETS_IN_95TH = "webrtc/video/packets/in/95th"

    WEBRTC_VIDEO_PACKETS_IN_99TH = "webrtc/video/packets/in/99th"

    WEBRTC_VIDEO_PACKETS_IN_AVG = "webrtc/video/packets/in/avg"

    WEBRTC_VIDEO_PACKETS_IN_MAX = "webrtc/video/packets/in/max"

    WEBRTC_VIDEO_PACKETS_IN_RSTDDEV = "webrtc/video/packets/in/rstddev"

    WEBRTC_VIDEO_PACKETS_IN_STDDEV = "webrtc/video/packets/in/stddev"

    WEBRTC_VIDEO_PACKETS_IN_TOTAL = "webrtc/video/packets/in/total"

    WEBRTC_VIDEO_PACKETS_OUT_25TH = "webrtc/video/packets/out/25th"

    WEBRTC_VIDEO_PACKETS_OUT_50TH = "webrtc/video/packets/out/50th"

    WEBRTC_VIDEO_PACKETS_OUT_75TH = "webrtc/video/packets/out/75th"

    WEBRTC_VIDEO_PACKETS_OUT_95TH = "webrtc/video/packets/out/95th"

    WEBRTC_VIDEO_PACKETS_OUT_99TH = "webrtc/video/packets/out/99th"

    WEBRTC_VIDEO_PACKETS_OUT_AVG = "webrtc/video/packets/out/avg"

    WEBRTC_VIDEO_PACKETS_OUT_MAX = "webrtc/video/packets/out/max"

    WEBRTC_VIDEO_PACKETS_OUT_RSTDDEV = "webrtc/video/packets/out/rstddev"

    WEBRTC_VIDEO_PACKETS_OUT_STDDEV = "webrtc/video/packets/out/stddev"

    WEBRTC_VIDEO_PACKETS_OUT_TOTAL = "webrtc/video/packets/out/total"

    WEBRTC_VIDEO_RTT_25TH = "webrtc/video/rtt/25th"

    WEBRTC_VIDEO_RTT_50TH = "webrtc/video/rtt/50th"

    WEBRTC_VIDEO_RTT_75TH = "webrtc/video/rtt/75th"

    WEBRTC_VIDEO_RTT_95TH = "webrtc/video/rtt/95th"

    WEBRTC_VIDEO_RTT_99TH = "webrtc/video/rtt/99th"

    WEBRTC_VIDEO_RTT_AVG = "webrtc/video/rtt/avg"

    WEBRTC_VIDEO_RTT_MAX = "webrtc/video/rtt/max"

    WEBRTC_VIDEO_RTT_RSTDDEV = "webrtc/video/rtt/rstddev"

    WEBRTC_VIDEO_RTT_STDDEV = "webrtc/video/rtt/stddev"

    def __str__(self):
        return self.value

    @staticmethod
    def from_json(jv: str) -> MetricPath:
        return MetricPath(jv)

    def to_json(self) -> str:
        return self.value
