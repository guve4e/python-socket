import socket, ssl

from src.soket.soket import Socket

class SSLSocket(Socket):

    def __init__(self, host: str) -> None:
        super().__init__()

        self.host = host

        try:
            self.context = ssl.create_default_context()
            self.context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            self.context.verify_mode = ssl.CERT_REQUIRED
            self.context.check_hostname = True
            self.context.load_default_certs()
        except Exception as e:
            print(e)


    def getSocket(self) -> object:

        ssl_sock = self.context.wrap_socket(self.socket, server_hostname=self.host)


        return ssl_sock