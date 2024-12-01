
from django import forms

from .models import Reservation, Venue, AvailableVenue


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'date_start' : forms.widgets.DateInput(attrs={'type': 'date'}),
            'date_end' : forms.widgets.DateInput(attrs={'type': 'date'}),
        }

    def is_valid(self):
        valid = super().is_valid()

        # Double Check
        # 1: if no data was posted, cleaned_data won't exist - empty form submit
        # 2: if valid: all required fields (start + end) are valid // is not None
        if hasattr(self, 'cleaned_data') and valid:

            start_date = self.cleaned_data.get('date_start')
            end_date = self.cleaned_data.get('date_end')
            if end_date < start_date:
                self.add_error('date_end', 'End date must be greater than start date')
                valid = False

        return valid

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter venues to only include those in AvailableVenue
        available_venues = AvailableVenue.objects.values_list('a_venue', flat=True)
        self.fields['venue'].queryset = Venue.objects.filter(pk__in=available_venues)
        self.fields['reservation_id'].disabled = True