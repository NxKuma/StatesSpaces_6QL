from django.urls import path
from .views import ReservationListView, ReservationDetailView, ReservationCreateView
urlpatterns = [
    path('reservations/', ReservationListView.as_view(), name='reservations'),
    path('reservation/<int:pk>/', ReservationDetailView.as_view(), name='reservation'),
    path('reservation/create', ReservationCreateView.as_view(), name='create'),
]

app_name = 'reservation'