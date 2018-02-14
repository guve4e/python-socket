import socket

DOMAIN = {"AF_INET": socket.AF_INET}
TYPE = {
    "STREAM": socket.SOCK_STREAM,
    "DATAGRAM": socket.SOCK_DGRAM
}

class StatelessSocket(object):

    def __init__(self, host, port: int) -> None:
        """
        7 members:
        1.  domain, string: The family of protocols that is used
            as the transport mechanism. These values are constants
            such as AF_INET, PF_INET, PF_UNIX, PF_X25.
        2.  type- string: The type of communications between the two endpoints,
            typically SOCK_STREAM for connection-oriented protocols
            and SOCK_DGRAM for connectionless protocols.
        3.  protocol - string: Typically zero, this may be used to identify a variant of
            a protocol within a domain and type.
        4.  port- int: Fixnum port number, a string containing a port number,
            or the name of a service.
        5.  The identifier of a network interface −
                *   A string, which can be a host name, a dotted-quad address,
                    or an IPV6 address in colon (and possibly dot) notation
                *   A string "<broadcast>", which specifies an
                    INADDR_BROADCAST address.
                *   A zero-length string, which specifies INADDR_ANY, or
                *   An Integer, interpreted as a binary address in host byte order.
        5.  timeout int:
        6.  buff_size - int: the maximum amount of data to be received at once
        7.  socket- Socket Object
        """
        self.domain = DOMAIN['AF_INET']
        self.type = TYPE['STREAM']
        self.protocol = 0
        self.port = port
        self.host = host
        self.timeout = 10000
        self.buff_size = 4096
        self.socket = None
        self.is_open_communication = False
        self.is_connected = False
        self.response_raw = []
        self.request_raw = None
        self.bytes_sent = 0
        self.bytes_received = 0

        try:
            self.open_socket()
            self.setup_socket()
        except OSError:
            print("Problem opening Socket")
            print("Error{}".format(socket.error))
            self.close()

    def open_socket(self) -> None:
        """

        :return:
        """
        self.socket = socket.socket(self.domain, self.type)
        if self.host == "local":
            self.host = socket.gethostname()
        self.is_open_communication = True

    def setup_socket(self) -> None:
        """

        """
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
        while self.bytes_received < msg_len:
            chunk = self.socket.recv(self.buff_size)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            self.bytes_received = self.bytes_received + len(chunk)
        self.response_raw = b''.join(chunks)


    def get_response_raw(self):
        return self.response_raw

    def close(self) -> None:
        """
        Closes TCP resources
        :return:
        """
        self.socket.close()
