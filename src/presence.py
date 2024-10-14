
from pypresence import Presence as PyPresence

class Presence(PyPresence):
    def __init__(self, client_id: str) -> None:
        super().__init__(client_id=client_id)

    def connect(self) -> None:
        super().connect()

        print(f'Connected to RPC application [id={self.client_id}]')