import os
import time
from structs import pyrogram, telethon
clear = 'clear' if os.name != 'nt' else 'cls'

os.system(clear)

print("""
 ____ ____   ____ 
/ ___/ ___| / ___|
\___ \___ \| |    
 ___) |__) | |___ 
|____/____/ \____|

String Session Converter v1.1 by @rojserbest.
Licensed under MIT.
""")

time.sleep(1)

os.system(clear)

print("""
Select an action:

1. Convert from Telethon to Pyrogram.
2. Convert from Pyrogram to Telethon.
""")

action = input('> ')

if action not in ('1', '2'):
    print('\nInvalid action selected.')
    exit()
elif action == '1':
    string = input('\nString session: ')
    unpacked_data = telethon.unpack(string)
    user_id = input('User ID: ')

    try:
        user_id = int(user_id)
    except Exception:
        print('\nInvalid user ID.')
        exit()

    test_mode = input('Test? [N/y] ').lower() == 'y'
    is_bot = input('Bot? [N/y] ').lower() == 'y'
    print(test_mode)
    print(is_bot)
    result = pyrogram.pack(
        unpacked_data['key'],
        unpacked_data['dc_id'],
        user_id,
        test_mode,
        is_bot
    )
elif action == '2':
    string = input('\nString session: ')
    unpacked_data = pyrogram.unpack(string)

    wss = input('wss? [Y/n] ').lower() == 'n'
    result = telethon.pack(unpacked_data['key'], unpacked_data['dc_id'], wss)


print(f'Result: {result}')
