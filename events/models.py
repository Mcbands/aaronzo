from django.db import models
from django.db import transaction
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.db.models import Sum, F




class Event(models.Model):
    EVENT_TYPES = [
        ('conference', 'Conference'),
        ('seminar', 'Seminar'),
        ('workshop', 'Workshop'),
        ('concert', 'Concert'),
        ('exhibition', 'Exhibition'),
        ('networking', 'Networking Event'),
        ('meetup', 'Meetup'),
        ('party', 'Party'),
        ('wedding', 'Wedding'),
        ('sports', 'Sports Event'),
        ('fundraiser', 'Fundraiser'),
        ('webinar', 'Webinar'),
        ('hackathon', 'Hackathon'),
        ('launch', 'Product Launch'),
        ('training', 'Training'),
        ('award_ceremony', 'Award Ceremony'),
        ('art_show', 'Art Show'),
        ('book_signing', 'Book Signing'),
        ('film_screening', 'Film Screening'),
        ('food_tasting', 'Food Tasting'),
        ('festival', 'Festival'),
        ('charity', 'Charity Event'),
        ('community', 'Community Event'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='organized_events')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='conference')
    image = models.ImageField(upload_to='static/images/events', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def reduce_ticket_quantities(self, num_tickets, ticket_type):
        # Get an available ticket for the event and ticket type
        available_ticket = Ticket.objects.filter(
            event=self, status='available', ticket_type=ticket_type
        ).first()

        if available_ticket and available_ticket.total_quantity >= num_tickets:
            # Update total_quantity and sold_quantity for the available ticket
            available_ticket.total_quantity -= num_tickets
            available_ticket.sold_quantity += num_tickets
            available_ticket.save()

            return True
        else:
            return False
    def get_vip_price(self, ticket_type):
        # Assuming you have a related_name for tickets in your Event model
        vip_ticket = self.tickets.filter(ticket_type='VIP').first()
        return vip_ticket.price if vip_ticket else 0

    def get_regular_price(self, ticket_type):
        # Assuming you have a related_name for tickets in your Event model
        regular_ticket = self.tickets.filter(ticket_type='Regular').first()
        return regular_ticket.price if regular_ticket else 0


    def num_available_tickets(self):
        # Calculate the total number of available tickets for each ticket type
        vip_tickets = self.tickets.filter(ticket_type='VIP').aggregate(total_quantity=Sum('total_quantity'))['total_quantity'] or 0
        regular_tickets = self.tickets.filter(ticket_type='Regular').aggregate(total_quantity=Sum('total_quantity'))['total_quantity'] or 0

        return {'VIP': vip_tickets, 'Regular': regular_tickets}

    def __str__(self):
        return self.title


class Ticket(models.Model):
    REGULAR = 'Regular'
    VIP = 'VIP'
    # Add more ticket types as needed

    TICKET_TYPE_CHOICES = [
        (REGULAR, 'Regular'),
        (VIP, 'VIP'),
        # Add more choices as needed
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('purchased', 'Purchased'),
        # Add more choices as needed
    ]
 
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.CharField(max_length=50, choices=TICKET_TYPE_CHOICES)  # Use choices argument
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    total_quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])  # Adjust the max value as needed
    sold_quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])  # Adjust the max value as needed
    creator_email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=True)



    def __str__(self):
        return f"{self.event.title} - {self.ticket_type}"


class Booking(models.Model):
    REGULAR = 'Regular'
    VIP = 'VIP'
    TICKET_TYPE_CHOICES = [
        (REGULAR, 'Regular'),
        (VIP, 'VIP'),
        # Add more choices as needed
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='bookings')
    num_tickets = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    ticket_type = models.CharField(max_length=50, choices=TICKET_TYPE_CHOICES, default="Regular")
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.email} - {self.event.title} - {self.num_tickets} tickets"
