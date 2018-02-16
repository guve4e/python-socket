from unittest import TestCase
from src.http_raw.http_request_socket import HttpRequestSocket

class TestHttpRequestSocket(TestCase):

    try:
        http = HttpRequestSocket()
     #   http.set_url("http://webapi.ddns.net/index.php/mockcontroller/1001")
        http.set_url("http://www.example.com")
        http.set_content_type("text/html")
        http.add_header("Transfer-encoding", "chunked")
        http.add_header("Connection", "close")
        http.send()

    except Exception as e:
        print (e)

