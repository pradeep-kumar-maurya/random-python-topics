import http.server
import ssl

# Define server address and port
server_address = ('', 4443)  # Host on port 4443

# Create a simple HTTP server
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap the server in SSL to use our self-signed certificate
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile='server.key',  # Path to your private key
    certfile='server.crt',  # Path to your self-signed certificate
    server_side=True
)

print("Server running on https://localhost:4443")
httpd.serve_forever()
