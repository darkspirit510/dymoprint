import cgi
import http.server
import os
import socketserver
import urllib
from http import HTTPStatus


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == 'index.html':
            self.path = 'index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/style.css':
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")

    def do_POST(self):
        postvars = self.read_post_vars()
        self.exec('python3 dymoprint -t ' + self.decode(postvars, b'height') + ' '
                  + self.str_or_nothing(self.decode(postvars, b'line1'))
                  + self.str_or_nothing(self.decode(postvars, b'line2'))
                  )

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def decode(self, postvars, index):
        return postvars[index].decode("UTF-8")

    def str_or_nothing(self, decode):
        if len(decode) > 0:
            return '"' + decode + '" '
        else:
            return ''

    def exec(self, command):
        print(command)
        os.system(command)

    def read_post_vars(self):
        ctype, pdict = cgi.parse_header(self.headers['content-type'])

        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers["content-length"])
            postvars = dict(urllib.parse.parse_qsl(self.rfile.read(length), keep_blank_values=1))
        else:
            postvars = {}
        return postvars


# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
