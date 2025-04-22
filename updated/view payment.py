import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def payment_view(request):
    if request.method == 'POST':
        try:
            # Get the token from the front-end
            token = request.POST.get('stripeToken')

            # Create the charge
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents ($10.00)
                currency='usd',
                description='Payment for Property Rental',
                source=token,
            )
            return JsonResponse({"status": "success"})
        except stripe.error.CardError as e:
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        # Get the Stripe publishable key
        publishable_key = settings.STRIPE_TEST_PUBLIC_KEY
        return render(request, 'payments/payment_form.html', {'publishable_key': publishable_key})
