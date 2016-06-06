from django import forms
from django.forms import ModelForm
from bookings.models import Booking


class BookingForm(ModelForm):

    class Meta:
        model = Booking

        fields = ['customer', 'service', 'service_employee', 'booking_time', 'additional_information',
                  'registration_number']

        widgets = {'booking_time': forms.DateTimeInput(attrs={'class': 'booking_time'})}

    def submit(self):
        if self.is_valid():
            print 'valid'
        else:
            print 'invalid'
        return self.errors
