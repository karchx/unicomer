from django.db import models
from accounts.models import Accounts

class Transfers(models.Model):
    from_account_id = models.ForeignKey(Accounts,related_name='account_primary' ,on_delete=models.CASCADE)
    to_account_id = models.ForeignKey(Accounts, related_name='account_secondary', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)


    objects = models.Manager()
