from django.urls import path

from .views import ProfileUpdateView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', ProfileUpdateView.as_view(), name = 'profile-update'),
]

app_name = 'user_management'   