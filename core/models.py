from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# core.models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, phone, address, password=None, **extra_fields):
        """
        Create and return a regular user with an email, first name, last name, date of birth, phone, address, user type, and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user_type = extra_fields.pop('user_type', None)  # Remove 'user_type' from extra_fields
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            phone=phone,
            address=address,
            user_type=user_type,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, date_of_birth, phone, address, password=None, **extra_fields):
        """
        Create and return a superuser with an email, first name, last name, date of birth, phone, address, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, first_name, last_name, date_of_birth, phone, address, password=password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    CLEARING_AND_FORWARDING = 1
    GREAT_AMBITION_CONSTRUCTION = 2
    LOGISTICS_AND_TOURS = 3
    SUMCO_SECURITY = 4
    KWACHA_LOAN = 5
    PECHI_CASH_ADVANCE = 6

    USER_TYPE_CHOICES = [
        (CLEARING_AND_FORWARDING, 'Clearing And Forwarding'),
        (GREAT_AMBITION_CONSTRUCTION, 'Great Ambition Construction'),
        (LOGISTICS_AND_TOURS, 'Logistics And Tours'),
        (SUMCO_SECURITY, 'Sumco Security'),
        (KWACHA_LOAN, 'Kwacha Loan'),
        (PECHI_CASH_ADVANCE, 'Pechi Cash Advance'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'phone', 'address', 'user_type']

    def __str__(self):
        return self.email

