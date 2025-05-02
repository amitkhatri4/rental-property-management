from itsdangerous import URLSafeTimedSerializer
from django.conf import settings

def generate_token(email):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    return serializer.dumps(email, salt="email-confirm")

def verify_token(token, max_age=3600):  # 1 hour expiry
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    try:
        email = serializer.loads(token, salt="email-confirm", max_age=max_age)
        return email
    except Exception:
        return None
