import socket, ssl
from src.soket.soket import Socket

class SocketCommunication(object):

    def __init__(self, socket: Socket, host: str, port: int) -> None:

        self.port = port
        self.host = host
        self.socket = socket.getSocket()
        self.timeout = 1000
        self.buff_size = 4096
        self.connection = None

        self.is_open_communication = False
        self.is_connected = False
        self.response_raw = []
        self.request_raw = None
        self.bytes_sent = 0
        self.bytes_received = 0

        try:

            self.setup_socket()
        except OSError as ex:
            print("Problem opening Socket")
            print("Error{}".format(ex))
            self.close()

    def setup_socket(self) -> None:
        """

        """
        if self.host == "local":
            self.host = socket.gethostname()

        self.socket.settimeout(self.timeout)
        self.socket.connect((self.host, self.port))

    def send(self, msg) -> None:
        """
        Wrapper over __send and __receive
        :param msg: string to be decoded and sent
        :return:
        """
        if (self.socket is None):
            return


        msg_len = self.__send(msg)
        self.__receive(msg_len)

    def __message_encode(self, msg: any, type = "ascii"):
        """
        Byte encodes a string
        :param msg:
        :return:
        """
        if isinstance(any, str):
            return msg.encode()
        else:
            return msg.encode(type)

    def __send(self, msg: str) -> int:
        """
        :return:
        """
        msg = self.__message_encode(msg)
        msg_len = len(msg)

        while self.bytes_sent < msg_len:
            sent = self.socket.send(msg[self.bytes_sent:])
            if sent == 0:
                raise RuntimeError("Socket connection broken!")
            self.bytes_sent = self.bytes_sent + sent

        return msg_len

    def __receive(self, msg_len: int) -> None:
        """
        Receive data from the socket. The return value is a bytes
        object representing the data received. The maximum
        amount of data to be received at once is specified by self.buff_size
        :return:
        """
        chunks = []
        self.bytes_received = 0

        while True:
            chunk = None
            chunk = self.socket.recv(self.buff_size)
            self.bytes_received = self.bytes_received + len(chunk)

            if chunk:
                chunks.append(chunk)
            else:
                break

        self.response_raw = b''.join(chunks)

    def get_response_raw(self):
        return self.response_raw

    def close(self) -> None:
        """
        Closes TCP resources
        :return:
        """
        self.socket.close()
