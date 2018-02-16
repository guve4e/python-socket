from unittest import TestCase
from src.soket.soket import Socket
from src.soket.stateless_socket import SocketCommunication
from src.soket.ssl_socket import SSLSocket

class TestSocketCommunication(TestCase):
    def test_normal_socket(self):
        request = "GET /index.php/mockcontroller/1001 HTTP/1.1\r\nHost: webapi.ddns.net\r\nConnection: close\r\n\r\n"

        sock = None
        rev = None
        try:
            sock = SocketCommunication(Socket(), "webapi.ddns.net", 80)
            sock.send(request)
            rev = sock.get_response_raw()

        except OSError as e:
            print("Error opening socket {}".format(e))
        except Exception as e:
            print("Exception {}".format(e))
        finally:
            print(rev)
            sock.close()

        self.fail()

    def test_ssl_socket(self):

        request = "GET /index.php/mockcontroller/1001 HTTP/1.1\r\nHost: webapi.ddns.net\r\nConnection: close\r\n\r\n"

        sock = None
        try:
            sock = SocketCommunication(SSLSocket("https://google.com"), "https://google.com", 80)
            sock.send(request)
            rev = sock.get_response_raw()

        except OSError as e:
            print("Error opening socket {}".format(e))
        except Exception as e:
            print("Exception {}".format(e))
        finally:
            sock.close()

        self.fail()

