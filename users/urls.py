from django.urls import path
from .views import Register, LoginAPIView

urlpatterns = [
    path('register', Register.as_view(), name='api-register'),
    path('login', LoginAPIView.as_view(), name='api-login'),
]

