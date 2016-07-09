from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from bookings.models import Booking, Customer


class BookingForm(ModelForm):
    class Meta:
        model = Booking

        fields = ['customer', 'service', 'service_employee', 'booking_time', 'additional_information',
                  'registration_number']

        widgets = {'booking_time': forms.DateTimeInput(attrs={'class': 'booking_time'})}

    def submit(self):
        if self.is_valid():
            self.save()
            return {}
        else:
            return self.errors


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'phone', 'registration_number']

    def submit(self):
        if self.is_valid():
            self.save()
            return {}
        else:
            return self.errors


class UserRegistrationForm(UserCreationForm):
    def clean_password2(self):
        if len(self.cleaned_data.get('password1')) < 6:
            raise ValidationError('Password is too short.')
        return super(UserRegistrationForm, self).clean_password2()
