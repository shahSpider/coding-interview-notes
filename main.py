import jwt
import datetime

SECRET_KEY = "your-secret-key"

payload = {
    "user_id": 123,
    "username": "john_doe",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # token expires in 1 hour
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("JWT Token:", token)

try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("Decoded:", decoded)
except jwt.ExpiredSignatureError:
    print("Token expired")
except jwt.InvalidTokenError:
    print("Invalid token")

