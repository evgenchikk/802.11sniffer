import config
import exception
import make_report

from scapy.layers.dot11 import *

packet_type_to_scapy = {
    'ProbeReq': Dot11ProbeReq, 
    'ProbeResp': Dot11ProbeResp, 
    'Beacon': Dot11Beacon
}


def get_report_file():
    try:
        file = open(config.report_file_name, 'a+')
    except exception.OpenFileException('Can\'t open report file'):
        return None 
    return file


def init():
    make_report.report = get_report_file()
    if make_report.report == None:
        print('Open file error')
        exit()

    if make_report.report.tell() == 0:
        make_report.report.write('N;DATE TIME;SRC MAC;DST MAC;CHANNEL;INFO;PACKET TYPE;dBm SIGNAL;dBm NOISE\n')
    else:
        make_report.report.seek(0)
        make_report.line_n = sum(1 for _ in make_report.report)


def stop():
    make_report.report.close()


def print_usage():
    print('''
Usage:
python 802.11sniffer.py -i <interface> -t <packet types> -c <packet count> -o <output file name>

-i [--iface] <inteface>
    Default 'en0'
    Interface that is used to sniff packets

-t [--types] <packet types>
    Default 'ProbeReq, ProbeResp'
    Types of packets that will be captured

-c [--count] <packet count>
    Default 0 (infinity)
    Count of packets that will be captured

-o [--output] <output file name>
    Default 'report.csv'
    File for report

All parameters can be set in 'config.py' file
''')

usage = '''
Usage:
python 802.11sniffer.py -i <interface> -t <packet types> -c <packet count> -o <output file name>

-i [--iface] <inteface>
    Default 'en0'
    Interface that is used to sniff packets

-t [--types] <packet types>
    Default 'ProbeReq, ProbeResp'
    Types of packets that will be captured

-c [--count] <packet count>
    Default 0 (infinity)
    Count of packets that will be captured

-o [--output] <output file name>
    Default 'report.csv'
    File for report

All parameters can be set in 'config.py' file.
You should run this script with root access.
'''