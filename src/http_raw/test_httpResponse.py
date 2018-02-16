from unittest import TestCase
from src.http_raw.response import HttpResponse


class TestHttpResponse(TestCase):

    response_str = "HTTP/1.1 200 OK\r\n" + \
                   "Date: Tue, 13 Feb 2018 23:13:08 GMT\r\n" + \
                   "Server: Apache/2.4.18 (Ubuntu)\r\n" + \
                   "Vary: Accept-Encoding\r\n" + \
                   "Content-Length: 119\r\n" + \
                   "Connection: close\r\n" + \
                   "Content-Type: text/html; charset=UTF-8\r\n\r\n" + \
                   """{
                    "data": {
                        "controller": "Test",
                        "method": "GET",
                        "id": "1001"
                        },
                        "key": "value" }"""

    try:
        httprequest = HttpResponse(response_str.encode())
    except Exception as e:
        print(e)

    print(httprequest.decode("uft8"))
