from django.urls import path
from . import views
from .views import verify_khalti

urlpatterns = [
    path('verify-khalti/', verify_khalti, name='verify_khalti'),
    path('search/', views.search, name='search'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('<slug:category_slug>/<slug:property_slug>/', views.property_detail, name='property'),
]
