from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
from controller.router import APIGetRouter

STATIC_DIR = "static"

class HTTPRequestHandler(BaseHTTPRequestHandler):
  def _set_headers(self, content_type="text/html", status=200):
    self.send_response(status)
    self.send_header("Content-Type", f"{content_type}; charset=utf-8")
    self.end_headers()

  def do_GET(self):
    parsed = urlparse(self.path)
    path = parsed.path
    params = parse_qs(parsed.query)

    if path.startswith("/api/"):
      if self.command == "GET":
        APIGet = APIGetRouter()
        response = APIGet.get_handler(path[len("/api/"):], params)
        self._json_response(response)
        return

    if parsed.path == "/":
      self._serve_file("index.html")
    else:
      filepath = os.path.join(STATIC_DIR, parsed.path.lstrip("/"))
      if os.path.isfile(filepath):
          self._serve_file(parsed.path.lstrip("/"))
      else:
          self._set_headers(status=404)
          self.wfile.write(b"Not Found")
          
  def do_POST(self):
    parsed = urlparse(self.path)
    path = parsed.path
    params = parse_qs(parsed.query)

    if path.startswith("/api/"):
       if self.command == "POST":
        self.handle_api_post(path[len("/api/"):], params)
        return
       
  def _serve_file(self, filename):
    filepath = os.path.join(STATIC_DIR, filename)
    if not os.path.exists(filepath):
        self._set_headers(status=404)
        self.wfile.write(b"File not found")
        return

    ext = os.path.splitext(filename)[1]
    mime = {
        ".html": "text/html",
        ".js": "application/javascript",
        ".css": "text/css",
    }.get(ext, "application/octet-stream")

    self._set_headers(mime)
    with open(filepath, "rb") as f:
        self.wfile.write(f.read())
       
  def handle_api_post(self, subpath, params):
    # post method
    print("in progress")
  
  def _json_response(self, data, status=200):
      self._set_headers("application/json", status)
      self.wfile.write(json.dumps(data).encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8888), HTTPRequestHandler)
    print("Server running at http://localhost:8888")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()