from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Reservation, Agent
# from .forms import ReservationForm
from django.urls import reverse

from user_management.models import Profile

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation_list.html'

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'

class ReservationCreateView(CreateView):
    model = Reservation
    # form_class = ReservationForm
    template_name = 'reservation_create.html'

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     form.fields['owner'].initial = Profile.objects.get(user=self.request.user)
    #     form.fields['owner'].disabled = True
    #     return form

    def get_success_url(self):
        return reverse('reservation:reservations', kwargs={'pk': self.object.pk})

class AgentListView(ListView):
    model = Agent
    template_name = 'agent_list.html'