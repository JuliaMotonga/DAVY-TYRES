from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from bookings.forms import BookingForm
from bookings.models import Customer, Booking


def service_detail(request):
    context = {}
    customer = None
    if request.method == 'POST':
        if request.user:
            try:
                customer = Customer.objects.filter(user=request.user.id).values('id')[0]['id']
            except Exception:
                pass
            if customer:
                form_data = dict(request.POST)
                form_data = {item[0]: item[1][0] for item in form_data.iteritems()}
                form_data['customer'] = customer
                form = BookingForm(form_data)
                errors = form.submit()
        if not customer:
            return HttpResponse('Unauthorized', status=401)
        if not errors:
            return render(request, "services/booking-confirmed.html", form.cleaned_data)
    else:
        form = BookingForm()

    context['booking_form'] = form

    return render(request, "services/service-details.html", context)


def show_active_bookings(request):
    context = {}

    user = User.objects.filter(email='ben@test.com')[0]
    customer = Customer.objects.filter(user_id=user.id)[0]
    bookings = Booking.objects.filter(customer_id=customer.id)

    context['bookings'] = bookings
    context['customer'] = customer

    return render(request, "services/customer-bookings.html", context)


def services(request):
    context = {}

    return render(request, "services/service-categories.html", context)
