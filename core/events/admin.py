"""from django.contrib import admin
from .models import Event, Ticket, Booking
from import_export.admin import ImportExportModelAdmin

class TicketAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('event', 'ticket_type', 'price', 'status', 'total_quantity', 'sold_quantity', 'creator_email', 'is_active')
    list_filter = ('event', 'ticket_type', 'status', 'is_active')
    search_fields = ('event__title', 'ticket_type', 'status', 'creator_email')

class BookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('event', 'customer', 'num_tickets', 'ticket_type', 'booking_date')
    list_filter = ('event', 'ticket_type', 'booking_date', 'customer')
    search_fields = ('event', 'ticket_type', 'booking_date', 'customer')

class EventAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'time', 'location', 'organizer', 'event_type', 'is_active')
    list_filter = ('title', 'description', 'date','organizer', 'event_type')
    search_fields = ('title', 'description', 'date','organizer', 'event_type')


admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Booking, BookingAdmin) """