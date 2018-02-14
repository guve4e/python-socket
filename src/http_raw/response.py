
class HttpResponse(object):

    def __init__(self, response: str) -> None:

        self.http_version = None
        self.code = None
        self.message = None
        self.headers_list = []
        self.headers_dict = {}
        self.body = None

        self.__make_response(response)

    def __make_response(self, response: str) -> None:
        """
        Given response string it builds
        the HttpResponse object
        :return:
        """
        # split the response string into
        # request(request line + headers) and body
        request, body = self.__split_response(response)

        # process the response line and get back the headers
        # as list of strings
        headers = self.__process_response_line(request)

        # make dictionary from the headers list
        self.__process_headers(headers)

        # process the body
        self.__process_body(body)

    def __split_response(self, response: str):
        """

        :param response:
        :return:
        """
        response = response.split("\r\n\r\n")

        return response[0], response[1]

    def __process_response_line(self, response: str) -> []:
        """
        At this point the response
        is separated from the body
        split this report string to
        :param response: string representation of
        response line and headers
        :return:
        """

        # get response line + headers
        response = response.split("\r\n")

        # split the response line
        response_line = response[0].split(" ")

        # response line must be of length 3 [http_version, code, message]
        if len(response_line) > 3:
            raise Exception("Wrong response line !")

        self.http_version = response_line[0]
        self.code = response_line[1]
        self.message = response_line[2]

        # now that we have the response line
        # remove it and return the headers
        response.pop(0)

        return response

    def __process_headers(self, headers_list: []) -> None:
        """
        Converts list of header lines as strings
        to dictionary of header lines
        :param headers: list of header lines
        :return: void
        """
        headers_dict = {}

        for header in headers_list:
            key_value = header.split(": ")
            if len(key_value) > 2:
                raise Exception("Something is wrong with Header Strings!")

            headers_dict[key_value[0]] = key_value[1]

        self.headers_list = headers_list
        self.headers_dict = headers_dict

    def __process_body(self, body) -> None:
        """
        TODO Transfer-code: chunked
        :param body:
        :return:
        """
        self.body = body

    def __str__(self):
        response = "HTTP version: {}\n".format(self.http_version)
        response = response + "CODE        : {}\n".format(self.code)
        response = response  + "MESSAGE     : {}\n".format(self.message)
        response = response + "HEADERS: \n"
        for header in self.headers_list:
            response = response + header + "\n"

        response = response + "BODY:\n"
        response = response + self.body

        return response



