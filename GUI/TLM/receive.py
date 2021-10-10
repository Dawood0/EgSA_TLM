import socket
import os
import time


class Receiver:
    def __init__(
        self,
        host: str = "0.0.0.0",
        port: int = 5001,
        buffer: int = 4096,
        ext: str = ''
    ) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.buffer = buffer
        self.ext = ext
        self.sep = "<SEPARATOR>"
        self.s.settimeout(20.0)

    def __initialize(self) -> None:
        self.s.bind((self.host, self.port))
        self.s.listen(10)

        print(f"[*] Listening as [{self.host}:{self.port}]")

    def __end(self) -> None:
        self.s.close()

        print(f"[*] Closed [{self.host}:{self.port}]")

    @property
    def receive(self) -> str:
        self.__initialize()

        try:
            client_socket, address = self.s.accept()
        except socket.timeout as e:
            print('TIMED OUT')

        try:
            print(f"[+] [{address[0]}:{address[1]}] is connected.")
    
            try:
                received = client_socket.recv(self.buffer).decode()
                filename = received.split(self.sep)[0]
                filename = filename.replace('\\', '/')
                filename = filename.split('/')[-1]
            except:
                cnt = 0
                while os.path.exists(f'file_{cnt}.{self.ext}'):
                    cnt += 1
                filename = os.path.basename(f'file_{cnt}.{self.ext}')
    
            print(
                f"[↓] Receiving [{filename}] from [{address[0]}:{address[1]}]"
            )
    
            # if os.path.isfile(filename):
            #     os.remove(filename)
    
            with open(filename, mode="wb") as f:
                all_bytes = ''
                while True:
                    bytes_read = client_socket.recv(self.buffer)
                    if not bytes_read:
                        break
                    all_bytes += str(bytes_read)
                    f.write(bytes_read)
    
            # print(all_bytes)
            print(
                f"[✔] Received [{filename}] from [{address[0]}:{address[1]}]"
            )
    
            client_socket.close()
            self.__end()
    
            return filename,True
        except:
            return 'NO FILE RECEIVED!'


if __name__ == "__main__":
    receiver = Receiver(ext='txt')
    receiver.receive
