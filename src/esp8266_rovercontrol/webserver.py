from urlparse import urlparse, urlextract
try:
  import usocket as socket
except:
  import socket

class WebServer:
    """docstring for WebServer."""
    def __init__(self, config: dict, test):
        print("Starting Webserver...")
        self.socketobject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketobject.bind(('', 80))
        self.socketobject.listen(5)
        self.request = None
        self.conn = None
        self.endpoint_get = '/'
        self.params = {}
        self.config = config
        self.test = test
        print("Webserver started!")

    def serve_webpage(self):
        with open('htmlbase.html') as f: 
          htmlbase = f.read()
        html = htmlbase
        self.conn.send('HTTP/1.1 200 OK\n')
        self.conn.send('Content-Type: text/html\n')
        self.conn.send('Connection: close\n\n')
        self.conn.sendall(html)    
        self.conn.close()

    def handle_connection(self):
        self.conn, self.addr = self.socketobject.accept()
        print('Got a connection from %s' % str(self.addr))
        request = self.conn.recv(1024)
        self.request = str(request)
        print('Content = %s' % self.request)
        self.get_params()
        print('Params:\n')
        print(self.params)
        return self.endpoint_get, self.params

    def get_params(self):
        self.endpoint_get = urlextract(self.request)
        self.params = urlparse(self.endpoint_get)
        return self.params 