from django.contrib import admin

from davyhome.models import Catalogue
from bookings.models import AvailabilityCalender, Customer, Booking, Service, TimeRange


class CatalogueAdmin(admin.ModelAdmin):
    pass


class BookingAdmin(admin.ModelAdmin):
    search_fields = ['registration_number']
    list_display = ['customer', 'service', 'booking_time', 'status', 'registration_number']
    list_filter = ['status', 'service']


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('phone', 'registration_number', 'user__first_name', 'user__last_name', 'user__email')
    list_display = ('first_name', 'last_name', 'email', 'phone', 'activated', 'registration_number')

    @staticmethod
    def email(obj):
        return obj.user.email

    @staticmethod
    def first_name(obj):
        return obj.user.first_name

    @staticmethod
    def last_name(obj):
        return obj.user.last_name

    @staticmethod
    def activated(obj):
        return obj.user.is_active


class ServiceAdmin(admin.ModelAdmin):
    pass


class AvailabilityCalenderAdmin(admin.ModelAdmin):
    pass


class TimeRangeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(AvailabilityCalender, AvailabilityCalenderAdmin)
admin.site.register(TimeRange, TimeRangeAdmin)
