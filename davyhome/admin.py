from django.contrib import admin

from davyhome.models import Catalogue, Tyre, PriceRange, SaleValue
from bookings.models import AvailabilityCalender, Booking, Service, TimeRange, BaseUser


class CatalogueAdmin(admin.ModelAdmin):
    pass


class TyreAdmin(admin.ModelAdmin):
    pass


class PriceRangeAdmin(admin.ModelAdmin):
    pass


class SaleValueAdmin(admin.ModelAdmin):
    pass


class BookingAdmin(admin.ModelAdmin):
    search_fields = ['registration_number']
    list_display = ['customer', 'service', 'booking_time', 'status', 'registration_number']
    list_filter = ['status', 'service']


class ServiceAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'first_name', 'last_name', 'phone', 'registration_number']
    list_display = ['email', 'first_name', 'is_staff', 'phone', 'registration_number']
    list_filter = ['is_staff', 'is_active']
    pass

class AvailabilityCalenderAdmin(admin.ModelAdmin):
    pass


class TimeRangeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(BaseUser, UserAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(AvailabilityCalender, AvailabilityCalenderAdmin)
admin.site.register(TimeRange, TimeRangeAdmin)
admin.site.register(Tyre, TyreAdmin)
admin.site.register(PriceRange, PriceRangeAdmin)
admin.site.register(SaleValue, SaleValueAdmin)
