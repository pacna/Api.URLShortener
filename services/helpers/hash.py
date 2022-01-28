from hashids import Hashids

hash: Hashids = Hashids(salt="salt bae")


class HashHelper:
    def __init__(self, counter: int) -> None:
        self.counter = counter

    def create_hash(self) -> str:
        created_hash: str = hash.encode(self.counter)
        return created_hash
