import base64
import ipaddress
import struct

from datacenters import get_ipv4


def pack(key: str, dc_id: int, user_id: int, is_bot: bool = False, test_mode: bool = False):
    return base64.urlsafe_b64encode(
        struct.pack(
            ">B?256sI?",
            dc_id,
            test_mode,
            key,
            user_id,
            is_bot
        )
    ).decode().rstrip('=')


def unpack(string: str):
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
