from django import forms
from .models import Reservation, Venue, AvailableVenue

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'date_start': forms.widgets.DateInput(attrs={'type': 'date'}),
            'date_end': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

    def is_valid(self):
        valid = super().is_valid()

        if hasattr(self, 'cleaned_data') and valid:
            start_date = self.cleaned_data.get('date_start')
            end_date = self.cleaned_data.get('date_end')
            if start_date and end_date:
                if end_date < start_date:
                    self.add_error('date_end', 'End date must be greater than start date')
                    valid = False
            else:
                if not start_date:
                    self.add_error('date_start', 'Start date is required')
                if not end_date:
                    self.add_error('date_end', 'End date is required')

        return valid