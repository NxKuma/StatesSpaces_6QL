from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .models import Reservation, Agent
from .forms import ReserveForm

from user_management.models import Profile

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation_list.html'

    def get_queryset(self):
        # Get the logged-in user's profile
        profile = Profile.objects.get(user=self.request.user)
        
        # Filter reservations associated with the customer's profile
        customer = profile.customer
        return Reservation.objects.filter(customer=customer)

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if messages.get_messages(self.request):
            context['messages'] = messages.get_messages(self.request)
        return context

    def get_object(self):
        reservation_id = self.kwargs.get('pk')  # Get the reservation_id from the URL
        return get_object_or_404(Reservation, reservation_id=reservation_id)  # Look up by reservation_id
    
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReserveForm
    template_name = 'reservation_create.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        profile = Profile.objects.get(user=self.request.user)
        customer = profile.customer

        # Set customer field value and disable it
        form.fields['customer'].initial = customer
        form.fields['customer'].disabled = True

        # Generate a new reservation ID based on the total count of reservations
        existing_reservations = Reservation.objects.count()
        new_reservation_id = f"{existing_reservations + 1:05d}"
        form.fields['reservation_id'].initial = new_reservation_id
        form.fields['reservation_id'].disabled = True

        return form

    def form_valid(self, form):
        venue = form.cleaned_data['venue']
        date_start = form.cleaned_data['date_start']
        date_end = form.cleaned_data['date_end']

        existing_reservation = Reservation.objects.filter(
            venue=venue,
            date_start__lte=date_end,
            date_end__gte=date_start
        ).exists()

        if existing_reservation:
            form.add_error('venue', 'This venue is already booked for the selected dates.')
            return self.render_to_response(self.get_context_data(form=form))

        reservation = form.save()
        messages.success(self.request, f"Your reservation with ID {reservation.reservation_id} has been successfully booked!")
        return redirect('reservation:detail', pk=reservation.pk)

    def get_success_url(self):
        return reverse('reservation:reservations', kwargs={'pk': self.object.pk})
    
class AgentListView(ListView):
    model = Agent
    template_name = 'agent_list.html'