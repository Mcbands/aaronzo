from django import forms
from .models import Event, Ticket

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'organizer', 'event_type', 'image']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'organizer': forms.Select(attrs={'class': 'form-control'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
           'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

        
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Phone',
            'address': 'Address',
            'date_of_birth': 'Date of Birth',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'user_type': 'Account Type',
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'ticket_type', 'price', 'status', 'total_quantity', 'sold_quantity', 'creator_email']

        widgets = {
            'event': forms.Select(attrs={'class': 'form-control'}),
            'ticket_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'creator_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'total_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'sold_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'event': 'Event',
            'ticket_type': 'Ticket Type',
            'price': 'Price',
            'status': 'Status',
            'creator_email': 'Your Email',
            'total_quantity': 'Total Quantity',
            'sold_quantity': 'Sold Quantity',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add any additional customizations or logic here, if needed

    # Add any additional form methods or customizations as needed

class BookingForm(forms.Form):
    num_tickets = forms.IntegerField(min_value=1, label='Number of Tickets')
    ticket_type = forms.ChoiceField(choices=[('VIP', 'VIP'), ('Regular', 'Regular')], label='Ticket Type')
