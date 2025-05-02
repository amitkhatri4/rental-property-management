from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .utils import generate_token, verify_token
from django.conf import settings

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, email=email, password=password, is_active=False)
        user.save()

        token = generate_token(email)
        verification_link = request.build_absolute_uri(f'/verify-email/{token}/')

        send_mail(
            'Verify your email',
            f'Click the link to verify your account: {verification_link}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        messages.success(request, 'Please check your email to verify your account.')
        return redirect('login')  # or wherever you want

    return render(request, 'registration/register.html')
