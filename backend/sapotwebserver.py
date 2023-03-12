import os
import time
from pathlib import Path
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

basedir = Path(__file__).resolve().parent.parent
template = open(os.path.join(basedir, 'frontend/template', 'index.html'), 'r')

class Sapot(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(template.read().encode())
