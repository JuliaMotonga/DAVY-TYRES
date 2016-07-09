from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from bookings.forms import CustomerForm, UserRegistrationForm


def index(request):
    """Home page for Davy tyres"""
    return render_to_response("test/index.html")


def catalogue(request):
    context = {
                'tempvar1': "Hello World",
                'tempvar2': "Privet",
                'range': range(5),  # ie. [1, 2, 3, 4, 5]
                'examplenum': 'this is not 1',
                'examplelist': ['first', 'second', 'third'],
                'exampledict': {
                    'tempvar3': 'bonjour',
                    'tempvar4': 12345
                }
               }
    return render(request,"catalogue.html",context)


def auth_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin/')
    else:
        return HttpResponseRedirect('/logindenied/')
    # The login is authorised if its matches its value


def register(request, redirect=None):
    context = {}
    if request.method == 'POST':

        username = "{}_{}".format(request.POST.get('first_name'), request.POST.get('last_name'))
        user_form = UserRegistrationForm({'username': username,
                                      'password1': request.POST.get('password1'),
                                      'password2': request.POST.get('password2')
                                      })
        user_form.is_valid()
        # user_form.clean_password()
        1+1
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.email = request.POST.get('email')
            new_user.first_name = request.POST.get('first_name')
            new_user.last_name = request.POST.get('last_name')
            new_user.save()
            if new_user:
                customer_form = CustomerForm({'user': new_user.id,
                                              'phone': request.POST.get('phone'),
                                              'registration_number': request.POST.get('registration_number')
                                              })
                customer = customer_form.save()
        else:
            customer_form = CustomerForm()
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerForm()
    context['user_form'] = user_form
    context['customer_form'] = customer_form
    context['redirected_from'] = redirect
    return render(request, "registration/registration_page.html", context)


# def service_detail(request):
#     context = {}
#
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         errors = form.submit()
#         if not errors:
#             return render(request, "services/booking-confirmed.html", form.cleaned_data)
#     else:
#         form = BookingForm()
#
#     context['booking_form'] = form
#
#     return render(request, "services/service-details.html", context)

def login(request):
    context = {}
    return render(request, 'login.html', context)


def loggedin(request):
    context = {}
    return render(request, "succesful_login.html", context)


def logindenied(request):
    context = {}
    return render(request, "failed_login.html", context)

