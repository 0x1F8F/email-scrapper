# import pathlib

class Email:
    def __init__(self,dest: str = "emails.txt"):
        self.dest = dest
        self._len = 0

    def append(self,email: list[str]):
        assert(type(email)==type(list)) , "email must be iterable"
        self._len += len(email)
        with open(self.dest,"a") as f:
            f.write("\n".join(email))

    def __len__(self):
        return self._len

