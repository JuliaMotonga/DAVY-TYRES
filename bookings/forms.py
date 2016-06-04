from django.forms import ModelForm
from bookings.models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'service', 'service_employee', 'booking_time', 'status', 'additional_information',
                  'registration_number']


    #         customer = models.ForeignKey(Customer)
    # service = models.ForeignKey(Service)
    # service_employee = models.ForeignKey(User)
    # booking_time = models.DateTimeField()
    # status = models.CharField(choices=BOOKING_STATUS, default=BOOKING_STATUS[0], max_length=20)
    # additional_information = models.TextField()
    # registration_number = models.CharField(max_length=10, null=True)


