# This server host current directory in localhost, when User ask for README.md it return index.md

import http.server
import socketserver

PORT = 8787

class RequestChanger(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if 'README.md' in self.path:
            self.path = self.path.replace('README','index')
        print(f'Custom HTTP Server Changed {self.path}')
        super().do_GET()

handler = RequestChanger

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

