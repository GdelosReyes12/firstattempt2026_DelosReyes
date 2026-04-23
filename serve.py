import http.server
import socketserver
import mimetypes

# Ensure .js files are served with the correct MIME type
mimetypes.add_type('application/javascript', '.js')

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on 0.0.0.0 port {PORT} (http://localhost:{PORT}/) ...")
    httpd.serve_forever()
