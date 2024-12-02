from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .models import Reservation, Agent, Venue
from .forms import ReserveForm

from user_management.models import Profile

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        
        customer = profile.customer
        return Reservation.objects.filter(customer=customer)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for reservation in context['reservations']:
            building = reservation.venue.venuebuilding.building
            agent = building.get_assigned_agent()
            reservation.agent = agent 
        return context

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if messages.get_messages(self.request):
            context['messages'] = messages.get_messages(self.request)
        return context

    def get_object(self):
        reservation_id = self.kwargs.get('pk')  
        return get_object_or_404(Reservation, reservation_id=reservation_id) 
    
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReserveForm
    template_name = 'reservation_create.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        profile = Profile.objects.get(user=self.request.user)
        customer = profile.customer

        form.fields['customer'].initial = customer
        form.fields['customer'].disabled = True

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
        return redirect('reservation:detail', pk=reservation.reservation_id)

    def get_success_url(self):
        return reverse('reservation:reservations', kwargs={'pk': self.object.pk})
    
class AgentReservationsView(ListView):
    model = Reservation
    template_name = 'agent_reservations.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        agent_id = self.kwargs['pk']  # Get the agent ID from the URL
        agent = get_object_or_404(Agent, agent_id=agent_id)
        # Filter reservations based on venues associated with this agent
        return Reservation.objects.filter(
            venue__venuebuilding__building__agentBuilding__agent=agent
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agent'] = get_object_or_404(Agent, agent_id=self.kwargs['pk'])
        return context
    
class VenueDetailView(DetailView):
    model = Venue
    template_name = 'venue_detail.html'
    context_object_name = 'venue'

    def get_object(self):
        venue_id = self.kwargs.get('pk')  # Get the venue ID from the URL
        return get_object_or_404(Venue, pk=venue_id)  # Retrieve the venue object using its primary key

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venue = context['venue']
        # Access the amenities related to this venue
        amenities = venue.amenityVenue.all()  # This uses the reverse relationship
        context['amenities'] = amenities
        return context