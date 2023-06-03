from django.db import models
from accounts.models import Accounts

class CreditCard(models.Model):
    from_account = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    card_number = models.CharField()
    expiration_date = models.DateField()
    cvc = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)


    objects = models.Manager()
