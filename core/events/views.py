from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Event, Booking, Ticket
from .forms import EventForm, TicketForm, BookingForm
from django.shortcuts import render, get_object_or_404, redirect


def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Assuming you have methods to get VIP and Regular prices from the event
    vip_price = event.get_vip_price("VIP")
    regular_price = event.get_regular_price("Regular")
    # Call the num_available_tickets function to get the available tickets
    available_tickets = event.num_available_tickets()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            num_tickets = form.cleaned_data['num_tickets']
            ticket_type = form.cleaned_data['ticket_type']

            if event.reduce_ticket_quantities(num_tickets, ticket_type):
                # Create a new booking
                booking = Booking(event=event, customer=request.user, num_tickets=num_tickets, ticket_type=ticket_type)
                booking.save()

                return redirect('events')  # Redirect to a success page or another view
            else:
                form.add_error('num_tickets', 'Not enough available tickets.')
    else:
        form = BookingForm()

    context = {
        'form': form,
        'event': event,
        'vip_price': vip_price,
        'regular_price': regular_price,
        'event': event,
        'available_tickets': available_tickets,
    }

    return render(request, 'book_event.html', context)


def events(request):
    # Get the user account type if the user is authenticated
    user_account_type = None
    if request.user.is_authenticated:
        user_account_type = request.user.get_user_type_display()

    # Retrieve a collection of events
    events_collection = Event.objects.all()

    # Group events by type
    grouped_events = {}
    for event in events_collection:
        event_type = event.get_event_type_display()  # Assuming you have a 'type' field in your Event model
        if event_type not in grouped_events:
            grouped_events[event_type] = []
        grouped_events[event_type].append(event)

    context = {
        'user_account_type': user_account_type,
        'grouped_events': grouped_events,
    }

    return render(request, "events.html", context)


#Function to create an event
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect("/home")
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

# function to create a ticket
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            # Save the ticket
            ticket = form.save()
            # Redirect to a success page or do something else
            return redirect('events')
    else:
        # If it's a GET request, create a new form
        form = TicketForm()

    return render(request, 'create_ticket.html', {'form': form})