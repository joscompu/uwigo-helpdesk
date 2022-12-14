from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'state']
    list_display = ('title', 'description', 'state', 'create_date')
    list_filter = ['state', 'create_date']
    search_fields = ['title', 'description']


admin.site.register(Ticket, TicketAdmin)