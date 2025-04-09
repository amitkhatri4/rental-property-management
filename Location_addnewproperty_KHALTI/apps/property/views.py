from django.shortcuts import render, get_object_or_404
from .models import Property, Category

# 🔍 SEARCH VIEW
def search(request):
    query = request.GET.get('query', '')
    category_slug = request.GET.get('category', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    location = request.GET.get('location', '')

    properties = Property.objects.all()
    selected_category_title = ''

    if query:
        properties = properties.filter(title__icontains=query)

    if category_slug:
        properties = properties.filter(category__slug=category_slug)
        category = Category.objects.filter(slug=category_slug).first()
        if category:
            selected_category_title = category.title

    if min_price:
        try:
            properties = properties.filter(price__gte=int(min_price))
        except ValueError:
            pass

    if max_price:
        try:
            properties = properties.filter(price__lte=int(max_price))
        except ValueError:
            pass

    if location:
        properties = properties.filter(location__icontains=location)

    categories = Category.objects.all()

    return render(request, 'property/search.html', {
        'properties': properties,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'location': location,
        'categories': categories,
        'selected_category': category_slug,
        'selected_category_title': selected_category_title
    })


# 📁 CATEGORY VIEW
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    properties = Property.objects.filter(category=category)
    return render(request, 'property/category.html', {
        'category': category,
        'properties': properties
    })


# 🏠 PROPERTY DETAIL VIEW
def property_detail(request, category_slug, property_slug):
    category = get_object_or_404(Category, slug=category_slug)
    property_obj = get_object_or_404(Property, category=category, slug=property_slug)
    return render(request, 'property/property.html', {
        'property': property_obj
    })


from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm
from apps.registration.models import Customer

@login_required
def add_property(request):
    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        customer = Customer.objects.create(created_by=request.user, name=request.user.username)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.customer = customer
            property_obj.save()
            return redirect('dashboard')  # Adjust the redirect as needed
    else:
        form = PropertyForm()

    return render(request, 'property/add_property.html', {'form': form})
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def verify_khalti(request):
    if request.method == "POST":
        data = json.loads(request.body)
        token = data.get("token")
        amount = data.get("amount")
        property_id = data.get("property_id")

        headers = {
            "Authorization": "Key test_secret_key_58d4a6fbed8f4f4aa5a171d2f764cb44"
        }

        payload = {
            "token": token,
            "amount": amount
        }

        response = requests.post("https://khalti.com/api/v2/payment/verify/", data=payload, headers=headers)
        
        if response.status_code == 200:
            # Do any database operations if needed (e.g. record booking)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": response.json()})
