from django.urls import path

from .import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.index, name="index"),
    path("sign-up", views.sign_up, name="sign_up"),
    path("about", views.about_us, name="about"),
    path("contact", views.contact_us, name="contact"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("tickets", views.tickets, name="tickets"),
    path("profile", views.profile, name="profile"),
    path("bookings", views.bookings, name="bookings"),
    path("event-list", views.event_list, name="event_list"),
    
]