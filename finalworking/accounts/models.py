from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any custom fields you need, for now, we keep it simple
    pass
