from django.urls import path
from . import views


#urlpatterns for app cart
urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('success/', views.success, name='success'),
]