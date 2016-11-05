import http.server
import socketserver

PORT = 8000

class customHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self):
        return

    def do_GET(self):
        print('do_GET called!')

#Handler = customHandler
Handler  = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
