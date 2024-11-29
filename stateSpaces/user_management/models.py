from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.OneToOneField('reservations.Customer', on_delete=models.CASCADE)
    display_name = models.CharField(max_length = 63)
    email_address = models.EmailField(max_length = 254)

    def __str__(self):
        return self.display_name