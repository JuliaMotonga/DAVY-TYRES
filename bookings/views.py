from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bookings.forms import BookingForm
from bookings.models import Booking, BaseUser


def service_detail(request):
    context, errors, customer = {}, None, None
    if request.method == 'POST':
        if request.user:
            try:
                customer = BaseUser.objects.filter(id=request.user.id)[0]
            except Exception as e:
                pass
            if customer:
                form_data = dict(request.POST)
                form_data = {item[0]: item[1][0] for item in form_data.iteritems()}
                form_data['customer'] = customer.id
                form = BookingForm(form_data)
                form.fields['service_employee'].queryset = BaseUser.objects.filter(is_staff=True)
                errors = form.submit()
        if not customer:
            return redirect('/register/booking')
        if not errors:
            return render(request, "services/booking-confirmed.html", form.cleaned_data)
    else:
        form = BookingForm()
        form.fields['service_employee'].queryset = BaseUser.objects.filter(is_staff=True)

    context['booking_form'] = form

    return render(request, "services/service-details.html", context)


def show_active_bookings(request):
    context = {}

    user = User.objects.filter(email='ben@test.com')[0]
    customer = BaseUser.objects.filter(user_id=user.id)[0]
    bookings = Booking.objects.filter(customer_id=customer.id)

    context['bookings'] = bookings
    context['customer'] = customer

    return render(request, "services/customer-bookings.html", context)


def services(request):
    context = {}

    return render(request, "services/service-categories.html", context)
