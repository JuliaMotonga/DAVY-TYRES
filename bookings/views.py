from django.shortcuts import render
from bookings.forms import BookingForm


def service_detail(request):
    context = {}
    errors = None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        errors = form.submit()
    else:
        form = BookingForm()

    context['booking_form'] = form

    return render(request, "services/service-details.html", context)


def services(request):
    context = {}

    return render(request, "services/service-categories.html", context)
