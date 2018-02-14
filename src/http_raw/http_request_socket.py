
from src.http_raw.a_http_request import AHttpRequest
from urllib.parse import urlparse
from src.http_raw.response import HttpResponse
from src.soket.stateless_socket import StatelessSocket


class HttpRequestSocket(AHttpRequest):

    def __init__(self) -> None:

        self.http_version = "HTTP/1.1"
        self.url = {}
        self.body = ""
        self.method = "GET"
        self.headers = {}
        self.request_str = None
        self.response_str = None
        self.verbose = False

    def __make_headers(self) -> str:
        """

        :return:
        """
        headers_str = "Host: {}\r\n" .format(self.url['host'])

        for key, value in self.headers.items():
            headers_str = headers_str + "{}: {}\r\n".format(key, value)

        return headers_str

    def __constructHrrpRequest(self):
        """

        :return:
        """
        # check if everything needed is set up correctly
        if not self.url:
            raise Exception("Set URL first!")
        # first make the request line [method path http_version]
        request = "{0} {1} {2}\r\n".format(self.method, self.url['path'], self.http_version)
        # then make the headers
        request = request + self.__make_headers()
        # separate from body
        request = request + "\r\n\r\n"
        # TODO add body here!!!

        self.request_str = request

    def __parse_url(self, url):
        """
        TODO if scheme is not included
        TODO it does not return right values
        :param url:
        :return:
        """
        url = urlparse(url)
        self.url['host'] = url.netloc

        if url.path == '':
            self.url['path'] = '/'
        else:
            self.url['path'] = url.path

        self.url['params'] = url.params
        self.url['query'] = url.query

    def __retrieve_body(self):
        raw = self.response_str.split("")

    def set_url(self, url: str) -> None:
        self.__parse_url(url)

    def set_method(self, method: str) -> None:
        self.method = method

    def set_content_type(self, content_type: str) -> None:
        self.content_type = content_type

    def set_http_version(self, http_version: str):
        self.http_version = http_version

    def set_verbose(self, verbose) -> None:
        self.verbose = verbose

    def add_headers(self, headers: {}) -> None:
        self.headers = headers

    def add_header(self, field_name: str, field_value: str) -> None:
        """
        Adds key value to headers dict
        :param field_name:
        :param field_value:
        :return:
        """
        self.headers.update({field_name: field_value})

    def add_body(self, data: []) -> None:
        self.data = data

    def send(self) -> None:
        """

        :return:
        """
        self.__constructHrrpRequest()

        if (self.verbose):
            print(self)

        sock = None
        try:
            sock = StatelessSocket(self.url['host'], 80)
            sock.send(self.request_str)
            rev = sock.get_response_raw()
            self.response_str = rev

        except OSError as e:
            print("Error opening socket {}".format(e))
        finally:
            sock.close()


    def get_response_raw(self) -> None:
        return self.__retrieve_body()

    def get_response_json(self) -> None:
        return None

    def get_response_with_info(self) -> HttpResponse:
        """
        Return HttpResponse Object
        :return:
        """
        response = HttpResponse(self.response_str.decode('UTF-8'))
        return response


    def __str__(self):
        response = "HTTP version: {}\n".format(self.http_version)
        response = response + "METHOD      : {}\n".format(self.method)
        response = response  + "PATH        : {}\n".format(self.url['path'])
        response = response + "HEADERS: \n"

        for key, value in self.headers.items():
            response = response + key + ": " + value + "\n"

        response = response + "BODY:\n"
        response = response + self.body

        return response



