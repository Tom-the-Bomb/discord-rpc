import time
from os import getenv

from dotenv import load_dotenv

from .presence import Presence

def main(client_id: str, *, interval: int = 1) -> None:
    rpc = Presence(client_id)
    rpc.connect()

    start = end = 1

    while True:
        rpc.update(
            # main text
            details='(・o・)',
            # timer (time elapsed)
            start=start,
            end=end,
            # large image
            large_image='roohammerbig',
            large_text='Roo hammer',
            # party info
            state='别哭',
            party_size=[1, 1],
        )
        time.sleep(interval)
        end += interval

if __name__ == '__main__':
    load_dotenv()

    main(getenv('RPC_CLIENT_ID'))