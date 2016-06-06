from django.shortcuts import render, redirect
from bookings.forms import BookingForm


def service_detail(request):
    context = {}

    if request.method == 'POST':
        form = BookingForm(request.POST)
        errors = form.submit()
        if not errors:
            return render(request, "services/booking-confirmed.html", form.cleaned_data)
    else:
        form = BookingForm()

    context['booking_form'] = form

    return render(request, "services/service-details.html", context)


def services(request):
    context = {}

    return render(request, "services/service-categories.html", context)
