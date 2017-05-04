import threading
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import json

from services import twitter


class HTTPRequestHandler(BaseHTTPRequestHandler):

    twitter_service = twitter.Twitter()

    def do_GET(self):

        twitter_data = self.twitter_service.get_twitter_data_from_account();

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(twitter_data, ensure_ascii=False))
        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    allow_reuse_address = True

    def shutdown(self):
        self.socket.close()
        HTTPServer.shutdown(self)


class SimpleHttpServer():

    def __init__(self, ip, port):
        self.server = ThreadedHTTPServer((ip, port), HTTPRequestHandler)

    def start(self):
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

    def wait_for_thread(self):
        self.server_thread.join()

    def stop(self):
        self.server.shutdown()
        self.wait_for_thread()


if __name__ == '__main__':
    server = SimpleHttpServer("0.0.0.0", 8080)
    print "HTTP Server Running..."
    server.start()
    server.wait_for_thread()
