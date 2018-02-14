from src.http_raw.http_request_socket import HttpRequestSocket

def process(url):

    raw = None
    try:
        http = HttpRequestSocket()
        #   http.set_url("http://webapi.ddns.net/index.php/mockcontroller/1001")
        http.set_url(url)
    #    http.set_content_type("text/html")
    #    http.add_header("Transfer-encoding", "chunked")
        http.add_header("User-Agent", "curl/7.55.1")
        http.add_header("Accept", "*/*")
        http.add_header("Connection", "close")
        http.set_verbose(True)
        http.send()
 #       raw = http.get_response_raw()
        response = http.get_response_with_info()
        print(response)
    except Exception as e:
        print(e)

    return raw

if __name__ == "__main__":

    raw = process("http://webapi.ddns.net/index.php/mockcontroller")
    # raw = process("http://www.example.com")
    # raw = process("http://www.httpwatch.com/httpgallery/chunked/chunkedimage.aspx")

