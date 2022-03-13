from scapy.all import *

import utils
import config
import packet_capture
# import argparse

# def temp(p):
#     if p.haslayer(Dot11Beacon):
#         # print(dir(p))
#         print(p[Dot11].show2())
#         print(p[Dot11EltDSSSet].channel)
#         exit()


def main():
    utils.init()

    sniffer = AsyncSniffer(iface = config.interface, prn = packet_capture.packet_capture, monitor = True, count = config.packets_count)
    sniffer.start()
    print('Sniffing started')
    print('Input \'q\' to stop sniffing: ')
    if (input() == 'q'):
        sniffer.stop
        utils.stop()

    # sniff(iface=config.interface, prn=temp, monitor=True)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(usage = utils.usage)
    
    # parser.add_argument('-i', '--iface', type = str, required = True)
    # parser.add_argument('-t', '--types', type = str, required = True)
    # parser.add_argument('-c', '--count', type = int, required = False)
    # parser.add_argument('-o', '--output', type = int, required = False)


    # args = parser.parse_args()
    
    main()