from http.server import BaseHTTPRequestHandler, HTTPServer
import jwt
import json
import uuid

SECRET_KEY="secret123"
PORT=8000


users=[]

class RequestHandler(BaseHTTPRequestHandler):
    def _set_header(self,code=200):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_len=int(self.headers.get('Content-Length',0))
        body =self.rfile.read(content_len)
        data=json.loads(body)

        if self.path == "/signup":
            username=data.get("username")
            password=data.get("password")
            if any(user["username"] == username for user in users):
                self._set_header(400)
                self.wfile.write(json.dumps({"error": "USer Already Exists"}).encode())
                return
            
            users.append({"username": username, "password": password})
            token =jwt.encode({"username": username}, SECRET_KEY, algorithm="HS256")
            self._set_header()
            self.wfile.write(json.dumps({"token":token}).encode())



def run():
    print(f"Server running on port {PORT}...")
    server = HTTPServer(('', PORT), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    run()