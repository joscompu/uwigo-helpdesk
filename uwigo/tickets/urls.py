from django.urls import path
from . import views

app_name = "tickets"
urlpatterns = [
    path('', views.index, name="all"),
    path('ticket/create', views.CreateTicket.as_view(), name="create_ticket"),
]
