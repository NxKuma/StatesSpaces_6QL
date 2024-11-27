from django.urls import path

from .views import home
from . import views

urlpatterns = [  
    path('', home ,name='homepage'),
]

app_name = 'homepage'