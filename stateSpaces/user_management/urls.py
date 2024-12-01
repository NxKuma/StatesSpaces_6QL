from django.urls import path, include
from django.contrib.auth.views import LoginView

from .views import ProfileUpdateView, RegisterProfileView

urlpatterns = [
    path('', ProfileUpdateView.as_view(), name = 'profile-update'),
    path('register', RegisterProfileView.as_view(), name='register'),
]

app_name = 'user_management'   