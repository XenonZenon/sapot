import os
import time
import mimetypes
from pathlib import Path
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class Sapot(BaseHTTPRequestHandler):

    def do_GET(self):

        self.basedir = Path(__file__).resolve().parent.parent
        self.filepath = os.path.join(self.basedir, 'frontend/template')
        
        if self.path == '/':
            filename = self.filepath + '/index.html'
        else:
            filename = self.filepath + self.path

        self.send_response(200)
        if filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        elif filename[-5:] == '.json':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-4:] == '.ico':
            self.send_header('Content-type', 'image/x-icon')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as file:
            html = file.read()
            self.wfile.write(html)
