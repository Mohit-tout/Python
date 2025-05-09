from http.server import BaseHTTPRequestHandler, HTTPServer
import jwt
import uuid
import json
from datetime import datetime, timedelta
import random
import smtplib
from email.mime.text import MIMEText
from urllib.parse import parse_qs, urlparse

SECRET_KEY = "secret123"
PORT = 8000
OTP_EXPIRE_TIME = timedelta(minutes=5)

yusers = [
    {"username": "Admin", "email": "admin@gmail.com", "password": "admin123", "role": "admin"}
]
otps = {}
categories = []
products = []

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len)
        data = json.loads(body)

        if self.path == "/signup":
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            role = "user"  

            if not username or not email or not password:
                self._respond(400, {"error": "All fields are required"})
                return

            if any(u["email"] == email for u in yusers):
                self._respond(409, {"error": "User already exists"})
                return

            yusers.append({"username": username, "email": email, "password": password, "role": role})
            self._respond(200, {"message": "User registered"})

        elif self.path == "/login":
            email = data.get("email")
            password = data.get("password")

            user = next((u for u in yusers if u["email"] == email and u["password"] == password), None)
            if not user:
                self._respond(401, {"error": "Invalid credentials"})
                return

            token = jwt.encode({
                "username": user["username"],
                "email": user["email"],
                "role": user["role"],
                "exp": datetime.utcnow() + timedelta(hours=1)
            }, SECRET_KEY, algorithm="HS256")
            self._respond(200, {"message": "Login successful", "token": token})

        elif self.path == "/forgot":
            email = data.get("email")
            user = next((u for u in yusers if u["email"] == email), None)
            if not user:
                self._respond(404, {"error": "Email not found"})
                return

            otp = self._generate_otp()
            otps[email] = {"otp": otp, "expire": datetime.now() + OTP_EXPIRE_TIME}
            self._send_email(email, otp)
            self._respond(200, {"message": "OTP sent to email"})

        elif self.path == "/verify-otp":
            email = data.get("email")
            otp_input = data.get("otp")
            otp_record = otps.get(email)

            if otp_record and otp_record["otp"] == otp_input and otp_record["expire"] > datetime.now():
                self._respond(200, {"message": "OTP verified"})
            else:
                self._respond(400, {"error": "Invalid or expired OTP"})

        elif self.path == "/reset-password":
            email = data.get("email")
            new_password = data.get("new_password")
            otp_input = data.get("otp")
            otp_record = otps.get(email)

            if otp_record and otp_record["otp"] == otp_input and otp_record["expire"] > datetime.now():
                for user in yusers:
                    if user["email"] == email:
                        user["password"] = new_password
                        self._respond(200, {"message": "Password updated"})
                        return
            self._respond(400, {"error": "Invalid or expired OTP"})

        elif self.path == "/category":
            payload = self._is_authenticated()
            if not payload: return
            if payload["role"] != "admin":
                self._respond(403, {"error": "Only admin can add categories"})
                return

            name = data.get("name")
            if not name:
                self._respond(400, {"error": "Category name is required"})
                return

            categories.append({"id": str(uuid.uuid4()), "name": name})
            self._respond(200, {"message": "Category added"})

        elif self.path == "/product":
            payload = self._is_authenticated()
            if not payload: return
            if payload["role"] != "admin":
                self._respond(403, {"error": "Only admin can add products"})
                return

            name = data.get("name")
            category_id = data.get("category_id")
            description = data.get("description", "")
            if not name or not category_id:
                self._respond(400, {"error": "Name and category_id are required"})
                return

            products.append({
                "id": str(uuid.uuid4()),
                "name": name,
                "category_id": category_id,
                "description": description
            })
            self._respond(200, {"message": "Product added"})

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/products":
            filtered = products
            name = query.get("name", [None])[0]
            category_id = query.get("category_id", [None])[0]
            page = int(query.get("page", [1])[0])
            limit = int(query.get("limit", [10])[0])

            if name:
                filtered = [p for p in filtered if name.lower() in p["name"].lower()]
            if category_id:
                filtered = [p for p in filtered if p["category_id"] == category_id]

            start = (page - 1) * limit
            end = start + limit
            paginated = filtered[start:end]

            self._respond(200, {"products": paginated, "total": len(filtered)})

        elif path == "/categories":
            self._respond(200, {"categories": categories})

    def do_PUT(self):
        parsed = urlparse(self.path)
        path_parts = parsed.path.strip("/").split("/")
        if len(path_parts) == 2 and path_parts[0] == "category":
            category_id = path_parts[1]
            content_len = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_len)
            data = json.loads(body)
            payload = self._is_authenticated()
            if not payload: return
            if payload["role"] != "admin":
                self._respond(403, {"error": "Only admin can update categories"})
                return

            for category in categories:
                if category["id"] == category_id:
                    category["name"] = data.get("name", category["name"])
                    self._respond(200, {"message": "Category updated"})
                    return
            self._respond(404, {"error": "Category not found"})

    def do_DELETE(self):
        parsed = urlparse(self.path)
        path_parts = parsed.path.strip("/").split("/")
        if len(path_parts) == 2 and path_parts[0] == "category":
            category_id = path_parts[1]
            payload = self._is_authenticated()
            if not payload: return
            if payload["role"] != "admin":
                self._respond(403, {"error": "Only admin can delete categories"})
                return

            global categories
            categories = [cat for cat in categories if cat["id"] != category_id]
            self._respond(200, {"message": "Category deleted"})

    def _respond(self, code, message):
        self._set_headers(code)
        self.wfile.write(json.dumps(message).encode())

    def _generate_otp(self):
        return str(random.randint(1000, 9999))

    def _send_email(self, recipient_email, otp):
        try:
            sender_email = "svcesiddharth@gmail.com"
            sender_password = "hvmckxflfqcegvts"
            message = MIMEText(f"Your OTP is: {otp}")
            message['Subject'] = "OTP Verification"
            message['From'] = sender_email
            message['To'] = recipient_email

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Email sent to {recipient_email}")
        except Exception as e:
            print(f"Email failed: {e}")

    def _is_authenticated(self):
        auth_header = self.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            self._respond(401, {"error": "Unauthorized"})
            return None

        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            self._respond(401, {"error": "Token expired"})
        except jwt.InvalidTokenError:
            self._respond(401, {"error": "Invalid token"})
        return None

def run():
    print(f"Server running on port {PORT}...")
    server = HTTPServer(('', PORT), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    run()
