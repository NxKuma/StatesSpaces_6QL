from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import Profile
from .forms import RegisterForm


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['display_name', 'email_address']
    template_name = "registration/profile_update.html"

    def get_success_url (self):
        return reverse_lazy("home")
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    
class RegisterProfileView(CreateView):
    model = Profile
    form_class = RegisterForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        reg_user = form.save()
        user_profile = Profile.objects.get(user=reg_user)
        user_profile.email = form.cleaned_data.get('email')
        user_profile.display_name = form.cleaned_data.get('display_name')
        user_profile.save()
        reg_user.save()
        login(self.request, reg_user, backend="django.contrib.auth.backends.ModelBackend")
        return response
    
    def get_success_url(self):
        return reverse_lazy('user_management:index')