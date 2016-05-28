from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Booking(models.Model):
    BOOKING_STATUS = (
        ('CF', 'Confirmed'),
        ('CM', 'Completed'),
        ('UF', 'Unfulfilled'),
        ('CN', 'Canceled'),
    )

    customer = models.ForeignKey(Customer)
    service = models.ForeignKey(Service)
    service_employee = models.ForeignKey(User)
    booking_time = models.DateTimeField()
    status = models.CharField(choices=BOOKING_STATUS, default=BOOKING_STATUS[0])
    additional_information = models.TextField()

    def __unicode__(self):
        return self.customer.name


class Customer(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=10)

    def __unicode__(self):
        return "{}'s profile".format(self.user)


class Service(models.Model):
    time_allocated = models.ForeignKey(TimeRange)
    availability = models.ForeignKey(AvailabilityCalender)
    name = models.CharField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    @property
    def price(self):
        return "${}".format(self.cost)

    @property
    def time_length(self):
        return self.time_allocated.start - self.time_allocated.end


class AvailabilityCalender(models.Model):
    monday = models.ForeignKey(TimeRange, on_delete=models.CASCADE)
    tuesday = models.ForeignKey(TimeRange, on_delete=models.CASCADE)
    wednesday = models.ForeignKey(TimeRange, on_delete=models.CASCADE)
    thursday = models.ForeignKey(TimeRange, on_delete=models.CASCADE)
    friday = models.ForeignKey(TimeRange, on_delete=models.CASCADE)
    saturday = models.ForeignKey(TimeRange, on_delete=models.CASCADE)
    sunday = models.ForeignKey(TimeRange, on_delete=models.CASCADE)


class TimeRange(models.Model):
    start = models.TimeField()
    end = models.TimeField()
