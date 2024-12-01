# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.OneToOneField('reservations.Customer', on_delete=models.CASCADE)
    display_name = models.CharField(max_length = 63)
    email_address = models.EmailField(max_length = 254)

    def __str__(self):
        return self.display_name
    
    def get_absolute_url(self):
        return reverse('user_management:profile-update', args=[str(self.pk)])
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.email = instance.email
        if instance.is_superuser:
            user_profile.display_name = instance.username
        user_profile.save()

post_save.connect(create_user_profile, sender=User)