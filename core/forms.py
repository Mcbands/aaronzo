from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone", "address", "date_of_birth", "password1", "password2", "user_type"]

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'style': 'height: 20px;'}),
            'user_type': forms.Select(choices=CustomUser.USER_TYPE_CHOICES),
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

