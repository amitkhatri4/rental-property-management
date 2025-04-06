from .forms import PropertyForm, PropertyImageForm
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import CreateUserForm
from django.utils.text import slugify
from .models import Customer
from django.contrib.auth.decorators import login_required
from apps.property.models import Property
from .tokens import account_activation_token
from .forms import PropertyForm, PropertyImageForm
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            customer = Customer.objects.create(name=user.username, created_by=user)
            user = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    else:
        form = CreateUserForm

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('frontpage')
        else:
            messages.info(request, 'Username or password is incorrect!')

    context = {}
    return render(request, 'registration/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    customer = request.user.customer
    property = customer.property.all()
    bookings = customer.bookings.all()

    for booking in bookings:
        booking.customer_amount = 0
        booking.customer_paid_amount = 0
        booking.fully_paid = True

        for item in booking.items.all():
            if item.customer == request.user.customer:
                if item.customer_paid:
                    booking.customer_paid_amount += item.get_total_price()
                else:
                    booking.customer_amount += item.get_total_price()
                    booking.fully_paid = False

    return render(request, 'registration/profile.html', {'customer': customer, 'property': property, 'bookings': bookings})

@login_required
def add_property(request):
    # ✅ Ensure customer exists before using
    customer, created = Customer.objects.get_or_create(
        created_by=request.user,
        defaults={'name': request.user.username}
    )

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)

        if form.is_valid():
            property = form.save(commit=False)
            property.customer = customer  # ✅ use guaranteed customer
            property.slug = slugify(property.title)

            # Extract latitude and longitude
            latitude = request.POST.get('latitude', None)
            longitude = request.POST.get('longitude', None)

            property.latitude = latitude
            property.longitude = longitude
            property.save()

            return redirect('profile')
    else:
        form = PropertyForm()

    return render(request, 'registration/addProperty.html', {'form': form})


@login_required



def edit_property(request, pk):
    property_instance = Property.objects.get(pk=pk)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PropertyForm(instance=property_instance)

    return render(request, 'registration/edit_property.html', {'form': form, 'property_instance': property_instance})



@login_required
def edit_customer(request):
    customer = request.user.customer

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name:
            customer.created_by.email = email
            customer.created_by.save()

            customer.name = name
            customer.save()

            return redirect('profile')

    return render(request, 'registration/edit_profile.html', {'customer': customer})

