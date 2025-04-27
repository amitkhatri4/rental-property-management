# your_app/utils.py

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_verification_email(request, user):
    from django.utils.http import urlsafe_base64_encode
    from django.utils.encoding import force_bytes
    from .tokens import email_verification_token

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = email_verification_token.make_token(user)
    verification_link = f"http://{request.get_host()}/verify-email/{uid}/{token}/"

    mail_subject = 'Activate your account'
    message = render_to_string('email_verification.html', {
        'user': user,
        'verification_link': verification_link,
    })
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
