import random
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddToCartForm
from .models import Category, Property
from apps.cart.cart import Cart
# Create your views here.

@login_required
def search(request):
    query = request.GET.get('query', '')
    property = Property.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'property/search.html', {'property': property, 'query': query})

@login_required
def property(request, category_slug, property_slug):
    cart = Cart(request)
    property = get_object_or_404(Property, category__slug=category_slug, slug=property_slug)

    imagesstring = '{"thumbnail": "%s", "image": "%s", "id": "mainimage"},' % (property.get_thumbnail(), property.image.url)

    # for image in property.images.all():
    #     imagesstring += ('{"thumbnail": "%s", "image": "%s", "id": "%s"},' % (image.get_thumbnail(), image.image.url, image.id))

    # print(imagesstring)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(property_id=property.id, quantity=quantity, update_quantity=False)
            messages.success(request, 'The property was added to the cart.')

            return redirect('property', category_slug=category_slug, property_slug=property_slug)
    else:
        form = AddToCartForm()


    similar_property = list(property.category.property.exclude(id=property.id))
    if len(similar_property) >= 4:
        similar_property = random.sample(similar_property, 4)

    context = {
        'form': form,
        'property': property,
        'similar_property': similar_property,
        'imagesstring': "[" + imagesstring.rstrip(',') + "]"
    }

    return render(request, 'property/property.html', context)

@login_required
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'property/category.html', {'category': category})
