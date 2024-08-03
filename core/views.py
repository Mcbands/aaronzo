from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from events.models import Booking, Ticket, Event

#home page view

def index(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "about.html")

def contact_us(request):
    return render(request, "contact.html")


@login_required
def dashboard(request):
    # Get the current user
    user = request.user

    # Fetch user-specific data
    bookings = Booking.objects.filter(customer=user)
    events_created = Event.objects.filter(organizer=user)
    
    # Retrieve all tickets created by the user
    user_tickets = Ticket.objects.filter(creator_email=request.user.email)

    context = {
        'user': user,
        'bookings': bookings,
        'events_created': events_created,
        'user_tickets': user_tickets,
    }

    return render(request, "dashboard.html", context)



@login_required
def event_list(request):
    # Get the current user
    user = request.user

    events_created = Event.objects.filter(organizer=user)
    

    context = {
          'events_created': events_created,
           'user': user,
    }

    return render(request, "event_list.html", context)



@login_required
def bookings(request):
      # Fetch user-specific data
    bookings = Booking.objects.filter(customer=request.user.id)

    context = {
        'bookings': bookings,
    }

    return render(request, "bookings.html", context)


@login_required
def tickets(request):
    # Retrieve all tickets created by the user
    user_tickets = Ticket.objects.filter(creator_email=request.user.email)

    context = {
        'user_tickets': user_tickets,
    }

    return render(request, "tickets.html", context)


@login_required
def profile(request):
    return render(request, "profile.html")



def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/dashboard")
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})

