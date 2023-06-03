from django.urls import path
from .views import CreditCardView

urlpatterns = [
        path('creditcard', CreditCardView.as_view(), name='creditcard')
 ]
