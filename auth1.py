from http.server import BaseHTTPRequestHandler, HTTPServer
import jwt
import json
import uuid
from urllib.parse import urlparse, parse_qs

SECRET_KEY = "secret123"
PORT = 8000

users = []       
products = []    

class RequestHandler(BaseHTTPRequestHandler):
    def _set_header(self, code=200):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def _parse_body(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len)
        return json.loads(body)

    def _get_token(self):
        auth_header = self.headers.get('Authorization')
        if not auth_header:
            return None
        return auth_header.split(" ")[1]

    def _validate_token(self):
        token = self._get_token()
        if not token:
            return None
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload  
        except jwt.InvalidTokenError:
            return None

    def do_POST(self):
        data = self._parse_body()

        if self.path == "/signup":
            username = data.get("username")
            password = data.get("password")
            role = data.get("role")  

            if not username or not password or role not in ["admin", "user"]:
                self._set_header(400)
                self.wfile.write(json.dumps({"error": "Username, password, and valid role are required"}).encode())
                return

            if any(user["username"] == username for user in users):
                self._set_header(400)
                self.wfile.write(json.dumps({"error": "User already exists"}).encode())
                return

            users.append({"username": username, "password": password, "role": role})
            token = jwt.encode({"username": username, "role": role}, SECRET_KEY, algorithm="HS256")
            self._set_header()
            self.wfile.write(json.dumps({"message": "Signup successful", "token": token}).encode())

        elif self.path == "/products":
            user_info = self._validate_token()
            if not user_info:
                self._set_header(401)
                self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
                return

            if user_info.get("role") != "admin":
                self._set_header(403)
                self.wfile.write(json.dumps({"error": "Unauthorized - Admins only"}).encode())
                return

            product = {
                "id": str(uuid.uuid4()),
                "name": data.get("name"),
                "price": data.get("price"),
                "category": data.get("category"),
                "description": data.get("description")
            }

            products.append(product)
            self._set_header()
            self.wfile.write(json.dumps({"message": "Product added", "product": product}).encode())

    def do_GET(self):
        if self.path == "/products":
            user_info = self._validate_token()
            if not user_info:
                self._set_header(401)
                self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
                return

            self._set_header()
            self.wfile.write(json.dumps(products).encode())

def run():
    server = HTTPServer(('localhost', PORT), RequestHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()

run()
