import base64
import ipaddress
import struct

from datacenters import get_ipv4


def pack_telethon(dc_id: int, ip: str, port: int, key: str):
    ip = ipaddress.ip_address(ip).packed
    return '1' + base64.urlsafe_b64encode(
        struct.pack(
            f'>B{len(ip)}sH256s',
            dc_id,
            ip,
            port,
            key,
        ),
    ).decode('ASCII')


def unpack_pyrogram(string: str):
    dc_id, test_mode, key, user_id, is_bot = struct.unpack(
        '>B?256sI?',
        base64.urlsafe_b64decode(
            string + '=' * (-len(string) % 4),
        ),
    )
    return {
        'dc_id': dc_id,
        'test_mode': test_mode,
        'key': key,
        'user_id': user_id,
        'is_bot': is_bot,
    }


unpacked_data = unpack_pyrogram(input('Enter Pyrogram string session: '))
dc_id = unpacked_data['dc_id']
ip = get_ipv4(dc_id)
port = 80 if input('SSL? [Y/n] ').lower() == 'n' else 443
key = unpacked_data['key']
print('Telethon string session:\n' + pack_telethon(dc_id, ip, port, key))
