from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            with open("Wireshark/HTTP_Server/form.html", "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read())
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == "/submit":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode()
            data = urllib.parse.parse_qs(body)

            # Log the captured data
            print("Captured POST data:", data)

            self.send_response(200)
            self.end_headers()
            response = f"You submitted: {data}"
            self.wfile.write(response.encode())

host = ("0.0.0.0", 8080)
print(f"Serving HTTP on {host[0]}:{host[1]}")
httpd = HTTPServer(host, SimpleHandler)
httpd.serve_forever()