import base64
import ipaddress
import struct
from datacenters import get_ipv4


def pack(key: str, dc_id: int,  wss: bool = False):
    ip = ipaddress.ip_address(get_ipv4(dc_id)).packed
    return '1' + base64.urlsafe_b64encode(
        struct.pack(
            f'>B{len(ip)}sH256s',
            dc_id,
            ip,
            443 if wss else 80,
            key,
        ),
    ).decode('ASCII')


def unpack(string: str):
    if not string:
        raise Exception('Empty string')

    if string[0] != '1':
        raise Exception('Invalid string')

    string = string[1:]
    ip_len = 4 if len(string) == 352 else 16
    dc_id, ip, port, key = struct.unpack(
        '>B{}sH256s'.format(ip_len), base64.urlsafe_b64decode(string)
    )

    ip = ipaddress.ip_address(ip).compressed

    return {'dc_id': dc_id, 'ip': ip, 'port': port, 'key': key}
