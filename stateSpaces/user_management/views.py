from django.views.generic import UpdateView, View
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from reservations.models import Customer
from .forms import RegistrationForm
from .models import Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['display_name', 'email_address']
    template_name = "profile_update.html"

    def get_success_url (self):
        return reverse_lazy("home")
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            
            # Get the latest customer and determine the next customer_id
            latest_customer = Customer.objects.order_by('-customer_id').first()
            next_id = f"{int(latest_customer.customer_id) + 1:05d}" if latest_customer else "00001"
            
            # Split the display name into first and last name
            display_name_parts = form.cleaned_data['display_name'].split()
            
            # Handle cases where the name is only a single word (either first name or last name)
            if len(display_name_parts) == 1:
                customer_last_name = display_name_parts[0]
                customer_first_name = ''
            else:
                customer_last_name = display_name_parts[0]
                customer_first_name = display_name_parts[-1]
            
            # Create the customer
            customer = Customer.objects.create(
                customer_id=next_id,
                customer_first_name=customer_first_name,
                customer_last_name=customer_last_name,
                birth_date=form.cleaned_data['birth_date']
            )
            
            # Create the profile
            Profile.objects.create(
                user=user,
                customer=customer,
                display_name=form.cleaned_data['display_name'],
                email_address=form.cleaned_data['email']
            )
            
            login(request, user)
            return redirect('home')
        
        return render(request, 'register.html', {'form': form})