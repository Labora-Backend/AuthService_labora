import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt(user):
    payload = {
        "id": user.id,
        "username": user.username,
        "role": user.role,
        "exp": datetime.utcnow() + timedelta(days=1),
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
