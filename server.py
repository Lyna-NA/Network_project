from http.server import HTTPServer,BaseHTTPRequestHandler 

class Handler(BaseHTTPRequestHandler):
   
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = open('404-page/dist/index.html').read()
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


def main():
    PORT = 8000
    server =HTTPServer(('',PORT),Handler)
    print('Server running on port %s'% PORT)
    server.serve_forever()

if __name__=='__main__':
    main()


