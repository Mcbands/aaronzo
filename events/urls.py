from django.urls import path
from .import views

urlpatterns = [

     path("events", views.events, name="events"),
     path("create-event", views.create_event, name= "create_event"),
     path("create-ticket", views.create_ticket, name="create_ticket"),
     path('book-event/<int:event_id>/', views.book_event, name='book_event'),
     ]