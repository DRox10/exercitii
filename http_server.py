from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time
import cgi

# ip and port of server
HOST_NAME = '127.0.0.1'

# by default http server port is 8085
PORT_NUMBER = '8085'

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Last-Modified',
                         self.sate_time_string(time.time()))
        #send file cotent to client
        self.end_headers()
        
        
    def do_HEAD(self):
        self._set_headers()
        
    def do_GET(self):
        rootdir = os.path.dirname("""#FILE NAME""") # file location
        if self.path.find("isButtonPressed=true") != -1:
            try:
                if self.path.endswith('.html'):
                    json.dumps(x['name'])
                    #f = open(rootdir + self.path) #open file
                    self._set_headers()
                    self.wfile.write(bytes( "utf-8"))
                    f.close()
                    return
        
            except IOError:
                self.send_error(404, "file not found")
            
            
# DEF DO POST

def run():
    try:
        print('HTTP Server is starting...')
        server_address = (HOST_NAME, int(PORT_NUMBER))
        server = HTTPServer(server_address, MyHTTPRequestHandler)
        print ("HTTP Server running on http://{0}:{1}/ use <Ctrl-C> to stop.".format(HOST_NAME, PORT_NUMBER))
        server.serve_forever()
    except KeyboardInterrupt:
        print (" o <Ctrl-C> entered, stopping web server....")
        server.socket.close()


if __name__ == '__main__':
    """ Starting Python program """
    run()
elif __name__ == "my-httpserver":
    initialize()
else:
    print ("This program is bad configured, you should be call to the module....")