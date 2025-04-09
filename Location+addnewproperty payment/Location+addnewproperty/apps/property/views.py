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
