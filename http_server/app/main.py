from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os

# Setup logging
logging.basicConfig(filename='server.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class WebhookHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')

        # Print the body to the console
        print("Received POST request:")
        print(body)
        print("------------------------------")

        # Log the body of the received POST request to a file
        logging.info(body)

        # Send a basic response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Received')

def run(server_class=HTTPServer, handler_class=WebhookHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(f'Stopping server on port {port}...')

if __name__ == '__main__':
    # Fetch port from environment variable, default to 5000 if not set
    # by default this port is in use on MacBooks
    port = int(os.environ.get('SERVER_PORT', 5000))
    run(port=port)
