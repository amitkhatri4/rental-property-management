from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('<slug:category_slug>/<slug:property_slug>/', views.property_detail, name='property'),
]
