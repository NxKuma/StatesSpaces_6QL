from django.urls import path
from .views import ReservationListView, ReservationDetailView, ReservationCreateView
urlpatterns = [
    path('', ReservationListView.as_view(), name='list'),
    path('reservation/<str:pk>/', ReservationDetailView.as_view(), name='detail'),
    path('create/', ReservationCreateView.as_view(), name='create'),
]

app_name = 'reservation'