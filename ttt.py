
import socket
import sys


def retrieve_url(url):
    """1
    return bytes of the body of the document at url
    """
    host_and_path = parse_url(url)

    if host_and_path is None:
        return None

    response = socket_communication(host_and_path)
    return response


def parse_url(url):
    """
    Parse the url and return list contains host, path, and port
    """
    parse_list = []

    lenght = len(url)

    if url.find("http://", 0, 7) != -1:
        parse_list = (url[7:lenght].split("/", 1))
        if len(parse_list) < 2 or parse_list[1] == "":
            path = "/"
        else:
            path = "/" + parse_list[1]
        port_split = parse_list[0].split(":", 1)
        host = port_split[0]
        if len(port_split) == 2:
            port = int(port_split[1])
        else:
            port = 80
        host_path_port = [host, path, port]
        return host_path_port

    else:
        return None


def create_request(host_and_path):
    """
    Create an http request
    """
    request = ("GET " + host_and_path[1] +
               " HTTP/1.1\r\nHost:" + host_and_path[0] +
               "\r\nConnection: close\r\n\r\n")
    return request


def socket_communication(host_and_path):
    """
    Send request to server and returns the response body
    """
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mysocket.settimeout(10000)
        mysocket.connect((host_and_path[0], int(host_and_path[2])))
        request = create_request(host_and_path)
        #request = "GET /index.php/mockcontroller/1001 HTTP/1.1\r\nHost:webapi.ddns.net\r\nConnection: close\r\n\r\n"
        mysocket.send(request.encode())
    except socket.error:
        return None

    data_packets = []
    while True:
        data = None
        try:
            data = mysocket.recv(4096)

            if data:
                data_packets.append(data)
                data = None
                continue
            else:
                break
        except socket.error:
            return None

    data = b"".join(data_packets)

    if data.find(b"200 OK", 0, len(data)) != -1:

        data2 = data.split(b"\r\n\r\n", 1)
        if data2[0].find(b"Transfer-Encoding: chunked",
                         0, len(data2[0])) != -1:
            chunked_data = data2[1].split(b"\r\n0\r\n\r\n", 1)
            chunked_parsed = chunked_parser(chunked_data[0])
            return chunked_parsed
        return data2[1]

    if data.find(b"301 Moved Permanently", 0, len(data)) != -1:
        return manage_redirect(data)
    else:
        return None


def chunked_parser(chunked_data):
    """
    Remove the hexadecimal values in the data
    """
    split_hexadecimal = chunked_data.split(b"\r\n")
    parsed_chunk = []
    chunk2 = b''
    for chunk in split_hexadecimal:
        try:
            hexa = int(chunk, 16)
        except ValueError:
            if len(chunk) < hexa:
                chunk2 = chunk2 + chunk
                if len(chunk2) < hexa:
                    chunk2 = chunk2 + b'\r\n'
                    continue
                else:
                    chunk = chunk2
                    chunk2 = b''
            parsed_chunk.append(chunk)

    data = b"".join(parsed_chunk)
    return data


def manage_redirect(data):
    """
    Get the url from response header and returns the response body
    the new url
    """
    data2 = data.split(b"\r\n\r\n", 1)
    header_list = data2[0].split(b"\r\n")
    for header in header_list:
        if header.find(b"Location: ") != -1:
            header_split = header.split(b": ", 1)
            url = header_split[1].decode("UTF-8")
            return retrieve_url(url)
    return None


if __name__ == "__main__":
  # print( retrieve_url(sys.argv[1]))  # pylint: disable=no-member
  #retrieve_url("http://webapi.ddns.net/index.php/mockcontroller/1001")
  print(retrieve_url("http://www.example.com"))
  #retrieve_url("http://accc.uic.edu/contact")
  # retrieve_url("http://i.imgur.com/fyxDric.jpg")
  # retrieve_url("http://www.illinois.edu/doesnotexist")
  # retrieve_url("http://www.ifyouregisterthisforclassyouareoutofcontrol.com/")
  # retrieve_url("http://marvin.cs.uic.edu:8080/")
  # retrieve_url("http://www.httpwatch.com/httpgallery/chunked/chunkedimage.aspx")