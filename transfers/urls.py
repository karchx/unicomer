from django.urls import path
from .views import Transfers

urlpatterns = [
        path('transfer', Transfers.as_view(), name='transfers')
 ]
