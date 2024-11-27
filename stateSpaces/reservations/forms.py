
from django import forms

from .models import Reservation, Venue, AvailableVenue


# class VenueForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'
#         widgets = {
#             'stock_status': forms.Select(choices=Product.STATUS_CHOICES),
#         }


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter venues to only include those in AvailableVenue
        available_venues = AvailableVenue.objects.values_list('a_venue', flat=True)
        self.fields['venue'].queryset = Venue.objects.filter(pk__in=available_venues)
        self.fields['reservation_id'].disabled = True

