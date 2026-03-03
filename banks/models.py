from django.db import models
from django.contrib.auth.models import User

class Bank(models.Model):
    name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=100)
    institution_number = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(User,
                             on_delete=models.CASCADE ,
                             related_name='bank'
                             )

    def __str__(self):
        return f"{self.name} ({self.institution_number})"


class Branches(models.Model):
    bank = models.ForeignKey(Bank,
                             on_delete=models.CASCADE ,
                             related_name='branches'
                             )
    name = models.CharField(max_length=100)
    transit_num= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(default="admin@enigmatix.io")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.bank.name})"
