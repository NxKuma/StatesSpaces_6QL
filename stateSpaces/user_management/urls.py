from django.urls import path, include
from django.contrib.auth.views import LoginView

from .views import ProfileUpdateView

urlpatterns = [
    path('', ProfileUpdateView.as_view(), name = 'profile-update'),
]

app_name = 'user_management'   