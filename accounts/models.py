from django.db import models
from users.models import CustomUser

class Accounts(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)


    objects = models.Manager()
