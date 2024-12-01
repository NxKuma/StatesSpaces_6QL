# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Profile
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import RegistrationForm


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['display_name', 'email_address']
    template_name = "profile_update.html"

    def get_success_url (self):
        return reverse_lazy("home")
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login
from reservations.models import Customer
from .models import Profile
from .forms import RegistrationForm

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new User object
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            
            # Determine the next customer_id
            latest_customer = Customer.objects.order_by('-customer_id').first()
            next_id = f"{int(latest_customer.customer_id) + 1:05d}" if latest_customer else "00001"
            
            # Create the Customer object
            customer = Customer.objects.create(
                customer_id=next_id,
                customer_first_name=form.cleaned_data['display_name'].split()[0],
                customer_last_name=form.cleaned_data['display_name'].split()[-1],
                birth_date=form.cleaned_data['birth_date']
            )
            
            # Create the Profile and link to the User and Customer
            Profile.objects.create(
                user=user,
                customer=customer,
                display_name=form.cleaned_data['display_name'],
                email_address=form.cleaned_data['email']
            )
            
            # Log the user in and redirect to home
            login(request, user)
            return redirect('home')
        
        return render(request, 'registration/register.html', {'form': form})
