from datetime import datetime
# from scapy.all import *

from scapy.layers.dot11 import *

import make_report
import utils
import config


def packet_capture(packet):
    for p_type in config.packet_types:
        if packet.haslayer(utils.packet_type_to_scapy[p_type]):
            line = '{};{};{};{};{};{};{};{}\n'.format(
                    datetime.today().replace(microsecond = 0), # DATE TIME
                    packet.addr2, # SRC MAC
                    packet.addr1, # DST MAC
                    '' if not packet.haslayer(Dot11EltDSSSet) else packet[Dot11EltDSSSet].channel, # CHANNEL
                    packet[Dot11Elt].info.decode(), # NAME
                    p_type, # PACKET TYPE
                    packet.dBm_AntSignal, # SIGNAL
                    packet.dBm_AntNoise) # NOISE
            
            make_report.write_to_report(line)
