from django.urls import path
from .views import ReservationListView, ReservationDetailView, ReservationCreateView, AgentReservationsView

urlpatterns = [
    path('create/', ReservationCreateView.as_view(), name='create'),
    path('', ReservationListView.as_view(), name='list'),
    path('<str:pk>/', ReservationDetailView.as_view(), name='detail'),
    path('agent/<str:pk>/reservations/', AgentReservationsView.as_view(), name='agent_reservations'),
]

app_name = 'reservation'