import http.server
import socketserver
import os

PORT=8000
SERVER_NAME = os.getenv("SERVER_NAME", "Backend 1")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f"<h1>Hello from {SERVER_NAME}</h1>".encode())
        self.wfile.write(f"<p>This is {SERVER_NAME} responding</p>".encode())

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"serving on port {PORT} as {SERVER_NAME}")
    httpd.serve_forever()
