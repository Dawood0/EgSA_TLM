import socket
import os
import sys


class Sender:
    def __init__(
            self,
            host: str,
            file: str,
            port: int = 5001,
            buffer: int = 4096
    ) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.buffer = buffer
        self.sep = "<SEPARATOR>"
        self.file = os.path.join(sys.path[0], file)
        self.filesize = os.path.getsize(self.file)

    def __initialize(self) -> None:
        print(f"[*] Connecting to [{self.host}:{self.port}]")

        self.s.connect((self.host, self.port))

        print("[+] Connected.")

    def __end(self) -> None:
        self.s.close()

        print(f"[*] Closed [{self.host}:{self.port}]")

    @property
    def send(self) -> None:
        self.__initialize()

        print(
            f"[↑] Sending [{self.file}] to [{self.host}:{self.port}]"
        )

        self.s.send(f"{self.file}{self.sep}{self.filesize}".encode())

        with open(self.file, "rb") as f:
            while True:
                bytes_read = f.read(self.buffer)
                self.s.sendall(bytes_read)
                if not bytes_read:
                    break

        print(
            f"[✔] Sent [{self.file}] to [{self.host}:{self.port}]"
        )

        self.__end()


if __name__ == "__main__":
    import time

    while True:
        sender = Sender(host="10.10.225.63", file=r"F:\courses\Programming\All Python\Projects folder\EgSA_TLM\txt_files\encode.txt")
        sender.send
        time.sleep(5)
        # time.sleep(2)

        # os.system(f"type nul > commands.txt")

