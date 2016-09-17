import json
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.serializers.json import DjangoJSONEncoder
from bookings.forms import BookingForm
from bookings.models import Booking, BaseUser, Service

from django.http import HttpResponseForbidden

from davytyres import settings


def service_detail(request):
    context, errors, customer, form = {}, None, None, None
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
            service = Service.objects.filter(id=form.data['service'])[0]
            booking_time = form.data['booking_time']
            email_body = " Hi {}, your booking for {} has been set for {} if you would like to cancel, please visit " \
                         "http://{}/{}".format(customer.first_name, service.name, booking_time, settings.HOST_DOMAIN,
                                               'services/bookings')
            send_mail('Booking confirmation for {}.'.format(customer.first_name), email_body,
                      'no_reply@davytyres.co.nz', [customer.email])
            return render(request, "services/booking-confirmed.html", form.cleaned_data)
    else:
        form = BookingForm()
        form.fields['service_employee'].queryset = BaseUser.objects.filter(is_staff=True)

    services_struct = [{"name": service.name,
                        "id": service.id,
                        "time_slots": time_slots(service),
                        "days_of_week": days_of_week(service)
                        } for service in Service.objects.all()]

    context['services_calendar'] = json.dumps(services_struct, cls=DjangoJSONEncoder)
    context['booking_form'] = form

    return render(request, "services/service-details.html", context)


def days_of_week(service):
    a = service.availability
    return [
            {"monday": a.monday},
            {"tuesday": a.tuesday},
            {"wednesday": a.wednesday},
            {"thursday": a.thursday},
            {"friday": a.friday},
            {"saturday": a.saturday},
            {"sunday": a.sunday},
            ]


def time_slots(service):
    time_slots = service.time_slots.all()
    return [{
        "start": slot.start,
        "end": slot.end
     } for slot in time_slots]


def show_active_bookings(request, cancel=None):
    context = {}
    user = BaseUser.objects.filter(email=request.user.email)[0]

    if cancel:
        booking = Booking.objects.filter(id=cancel)[0]
        if booking.customer.id == request.user.id and booking.status[3] == 'C' and booking.status[4] == 'F':
            booking.status = Booking.BOOKING_STATUS[3]
            booking.save()
            email_body = "User {} has canceled booking #{}".format(user.email, booking.id)
            send_mail('Booking confirmation for {}.'.format(user.first_name), email_body, 'no_reply@davytyres.co.nz',
                      [settings.EMAIL_ADMIN_USER])
        else:
            return HttpResponseForbidden()
        # context['canceled'] = 'booking #{} was cancelled.'.format(booking.id)
    bookings = Booking.objects.filter(customer_id=user.id)

    context['bookings'] = bookings

    return render(request, "services/customer-bookings.html", context)


def services(request):
    context = {}

    return render(request, "services/service-categories.html", context)
