
class HttpRequest(object):

    def __init__(self,httpHttpRequestSocket ) -> None:
        """

        """
        self.url = url

        if not self.url:
            raise Exception("HttpRequest needs URL!")

        self.http_version = "HTTP/1.0"
        self.request_line = None
        self.body = None
        self.method = method
        self.headers = {}
        self.body = None
        self.request_str = None

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

    def __str__(self):
        response = "HTTP version: {}\n".format(self.http_version)
        response = response + "METHOD        : {}\n".format(self.method)
        response = response  + "PATH     : {}\n".format(self.url['path'])
        response = response + "HEADERS: \n"
        for header in self.headers:
            response = response + header + "\n"

        response = response + "BODY:\n"
        response = response + self.body

        return response