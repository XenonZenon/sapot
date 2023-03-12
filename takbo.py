from http.server import HTTPServer
from backend.sapotwebserver import Sapot

hostname = "localhost"
port = 8000

if __name__ == "__main__":
    sapot = HTTPServer((hostname, port), Sapot)
    print("Sapot started http://%s:%s" % (hostname, port))

    try:
        sapot.serve_forever()
    except KeyboardInterrupt:
        pass
    sapot.server_close()
    print("Sapot stopped.")
