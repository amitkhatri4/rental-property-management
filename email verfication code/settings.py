# settings.py

# Email backend settings (for development, you can use console backend)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'  # or your SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # NOT your normal password (use Gmail App Password if using Gmail)
DEFAULT_FROM_EMAIL = 'Your Site Name <your-email@gmail.com>'
