from django.urls import path
from .views import RegisterUserAPIView, LoginAPIView

urlpatterns = [
    path('register', RegisterUserAPIView.as_view(), name='api-register'),
    path('login', LoginAPIView.as_view(), name='api-login'),
]

