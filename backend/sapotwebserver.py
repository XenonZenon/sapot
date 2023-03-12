import os
import time
import mimetypes
from pathlib import Path
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class Sapot(BaseHTTPRequestHandler):

    def do_GET(self):

        self.basedir = Path(__file__).resolve().parent.parent
        self.template = os.path.join(self.basedir, 'frontend/template')
        self.static = os.path.join(self.basedir, 'frontend/static')

        if self.path == '/':
            filename = self.template + '/index.html'
        else:
            filename = self.static + self.path

        self.send_response(200)
        if filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        elif filename[-5:] == '.json':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-4:] == '.ico':
            self.send_header('Content-type', 'image/x-icon')
        elif filename[-4:] == '.svg':
            self.send_header('Content-type', 'image/svg+xml')
        elif filename[-4:] == '.png':
            self.send_header('Content-type', 'image/x-png')
        elif filename[-4:] == '.jpg':
            self.send_header('Content-type', 'image/jpeg')
        elif filename[-4:] == '.bmp':
            self.send_header('Content-type', 'image/bmp')
        elif filename[-4:] == '.avi':
            self.send_header('Content-type', 'video/x-msvideo')
        elif filename[-4:] == '.3gp':
            self.send_header('Content-type', 'video/3gpp')
        elif filename[-4:] == '.3g2':
            self.send_header('Content-type', 'video/3gpp2')
        elif filename[-4:] == '.mp4':
            self.send_header('Content-type', 'video/mp4')
        elif filename[-4:] == '.otf':
            self.send_header('Content-type', 'font/otf')
        elif filename[-4:] == '.woff':
            self.send_header('Content-type', 'font/woff')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as file:
            html = file.read()
            self.wfile.write(html)
