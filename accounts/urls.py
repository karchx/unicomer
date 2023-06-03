from django.urls import path
from .views import Accounts

urlpatterns = [
        path('accounts', Accounts.as_view(), name='accounts')
 ]
