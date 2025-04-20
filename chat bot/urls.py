from django.urls import path
from . import views

urlpatterns = [
    path('ask/', views.ask_chatbot, name='chatbot_ask'),  # URL for sending messages to the chatbot
]
