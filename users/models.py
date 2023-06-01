from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField("Name", max_length=240)
    lastname = models.CharField("LastName", max_length=240)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name