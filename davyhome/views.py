from binascii import hexlify, unhexlify
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from bookings.forms import RegistrationForm
from django.core.mail import send_mail

from bookings.models import BaseUser
from davytyres import settings


def index(request):
    """Home page for Davy tyres"""
    return render_to_response("test/index.html")


def test_view(request):
    return render(request, "test/testview.html", {})

def about_us(request):
    return render(request, "davytyres/about-us.html", {})

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
    return render(request, "test/catalogue.html", context)


def unimplemented(request):
    return render(request, "unimplemented.html")

def about_us(request):
    return render(request, "davytyres/about-us.html")


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
    user_form = RegistrationForm(request.POST or None)
    context['user_form'] = user_form

    if request.method == 'POST':
        valid = user_form.is_valid()
        if valid:
            user = user_form.save()
            email_body = " Hi {}, please activate your account " \
                         "by visiting this link http://{}/activate/{}/{}.".format(user.first_name,
                                                                                  settings.HOST_DOMAIN,
                                                                                  hexlify(user.confirmation_key),
                                                                                  hexlify(user.email))
            send_mail('user registration for {} at davytyres.co.nz'.format(user.first_name),
                      email_body, 'no_reply@davytyres.co.nz', [user.email])
            return render(request, 'registration/register-success.html', context)
        else:
            context['errors'] = user_form.errors

    return render(request, 'registration/registration_page.html', context)


def activate(request, *args, **kwargs):
    try:
        activation_key = unhexlify(kwargs['activation'])
        email = unhexlify(kwargs['email'])
        user = BaseUser.objects.filter(email=email)[0]
        user.confirm_email(activation_key)
    except Exception as e:
        return render(request, 'unimplemented.html')
    return render(request, 'registration/activated.html')


def login(request):
    context = {}
    return render(request, 'login.html', context)


def loggedin(request):
    context = {}
    return render(request, "registration/successful_login.html", context)


def logindenied(request):
    context = {'failed_login': True}
    return render(request, "registration/failed_login.html", context)

