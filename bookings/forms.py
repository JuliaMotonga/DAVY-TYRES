from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from bookings.models import Booking, BaseUser


class BookingForm(ModelForm):
    class Meta:
        model = Booking

        fields = ['customer', 'service', 'service_employee', 'booking_time', 'additional_information',
                  'registration_number']

        widgets = {'booking_time': forms.DateTimeInput()}

    def submit(self):
        if self.is_valid():
            self.save()
            return {}
        else:
            return self.errors


class RegistrationForm(UserCreationForm):
    class Meta:
        model = BaseUser

        fields = ['first_name', 'last_name', 'email', 'phone', 'registration_number']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.registration_number = self.cleaned_data['registration_number']
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return self.is_valid()

