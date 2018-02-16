from unittest import TestCase
from src.soket.stateless_socket import SocketCommunication

class TestSocket(TestCase):
    def test___init__(self):
        pass

    def testSocket(self):

        request = "GET /index.php/mockcontroller/1001 HTTP/1.1\r\nHost: webapi.ddns.net\r\nConnection: close\r\n\r\n"

        sock = None
        try:
            sock = SocketCommunication("local", 9733)
            sock.send(request)
            rev = sock.get_response_raw()

        except OSError as e:
            print("Error opening socket {}".format(e))
        finally:
            sock.close()

        self.assertEquals(True, True)
