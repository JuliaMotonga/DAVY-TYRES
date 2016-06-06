from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class TimeRange(models.Model):
    name = models.CharField(max_length=20, null=True, )
    start = models.TimeField()
    end = models.TimeField()

    def __unicode__(self):
        return self.name


class AvailabilityCalender(models.Model):
    name = models.CharField(max_length=30)
    monday = models.ForeignKey(TimeRange, related_name='monday_time_range', on_delete=models.CASCADE)
    tuesday = models.ForeignKey(TimeRange, related_name='tuesday_time_range', on_delete=models.CASCADE)
    wednesday = models.ForeignKey(TimeRange, related_name='wednesday_time_range', on_delete=models.CASCADE)
    thursday = models.ForeignKey(TimeRange, related_name='thursday_time_range', on_delete=models.CASCADE)
    friday = models.ForeignKey(TimeRange, related_name='friday_time_range', on_delete=models.CASCADE)
    saturday = models.ForeignKey(TimeRange, related_name='saturday_time_range', on_delete=models.CASCADE)
    sunday = models.ForeignKey(TimeRange, related_name='sunday_time_range', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=10)

    def __unicode__(self):
        return self.user.username


class Service(models.Model):
    time_allocated = models.ForeignKey(TimeRange)
    availability = models.ForeignKey(AvailabilityCalender)
    name = models.CharField(max_length=30)
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
    status = models.CharField(choices=BOOKING_STATUS, default=BOOKING_STATUS[0], max_length=20)
    additional_information = models.TextField()
    registration_number = models.CharField(max_length=10, null=True)

    def __unicode__(self):
        return "{}'s booking".format(self.customer.user.username)



