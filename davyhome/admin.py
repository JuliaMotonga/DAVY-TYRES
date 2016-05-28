from django.contrib import admin

from davyhome.models import Catalogue
from bookings.models import AvailabilityCalender, Customer, Booking, Service, TimeRange


class CatalogueAdmin(admin.ModelAdmin):
    pass


class BookingAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


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
