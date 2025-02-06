from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def homepage(request):
    return render(request, 'core/homePage.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # send email
        send_mail(
            'Message from ' + name,
            message,
            email,
            ['sandipkhadka9810@gmail.com', email],
        )

        return render(request, 'core/contact.html', {'name': name})

    else:
        return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')