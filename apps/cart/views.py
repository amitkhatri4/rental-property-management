from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .cart import Cart
from .forms import CheckoutForm

from apps.booking.utilities import checkout, notify_landlord, notify_customer

@login_required
def cart_detail(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            zipcode = form.cleaned_data['zipcode']
            place = form.cleaned_data['place']

            booking = checkout(request, first_name, last_name, email, address, zipcode, place, phone,
                             cart.get_total_cost())

            cart.clear()

            notify_landlord(booking)
            notify_customer(booking)

            return redirect('success')
    else:
        form = CheckoutForm()

    remove_from_cart = request.GET.get('remove_from_cart', '')

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')

    return render(request, 'cart/cart.html', {'form': form})

@login_required
def success(request):
    return render(request, 'cart/success.html')