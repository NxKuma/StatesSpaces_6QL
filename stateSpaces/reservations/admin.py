from django.contrib import admin

# Register your models here.
from .models import AvailableVenue

class AvailableVenueAdmin(admin.ModelAdmin):
    model = AvailableVenue

admin.site.register(AvailableVenue, AvailableVenueAdmin)