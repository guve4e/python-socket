import socket

DOMAIN = {"AF_INET": socket.AF_INET}
TYPE = {
    "STREAM": socket.SOCK_STREAM,
    "DATAGRAM": socket.SOCK_DGRAM
}

class Socket(object):

    def __init__(self) -> None:
        """
               4 members:
               1.  domain, string: The family of protocols that is used
                   as the transport mechanism. These values are constants
                   such as AF_INET, PF_INET, PF_UNIX, PF_X25.
               2.  type- string: The type of communications between the two endpoints,
                   typically SOCK_STREAM for connection-oriented protocols
                   and SOCK_DGRAM for connectionless protocols.
               3.  protocol - string: Typically zero, this may be used to identify a variant of
                   a protocol within a domain and type.

               4.  socket- Socket Object
               """
        self.domain = DOMAIN['AF_INET']
        self.type = TYPE['STREAM']
        self.protocol = 0

        self.socket = None

        try:
            self.__open_socket()

        except OSError as ex:
            print("Problem opening Socket")
            print("Error{}".format(ex))


    def __open_socket(self) -> None:
        """

        :return:
        """
        self.socket = socket.socket(self.domain, self.type)

        self.is_open_communication = True

    def getSocket(self) -> object:
        return self.socket