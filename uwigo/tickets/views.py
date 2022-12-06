from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Ticket


def index(request):
    list_of_tickets = Ticket.objects.all()
    return render(request, 'tickets/index.html', {
        'list_of_tickets': list_of_tickets
    })


def detail(request, id):
    detail = get_object_or_404(Ticket, id)
    return render(request, 'tickets/detail.html', {
        'detail': detail
    })
    

class CreateTicket(CreateView):
    model = Ticket
    template_name = 'tickets/create.html'
    fields = ['title', 'description', 'state']
    success_url = '/'
