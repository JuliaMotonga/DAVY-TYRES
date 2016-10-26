from binascii import hexlify, unhexlify
from django.contrib import auth
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from bookings.forms import RegistrationForm
from django.core.mail import send_mail

from bookings.models import BaseUser
from davyhome.forms import TyreForm
from davyhome.models import Tyre
from davytyres import settings


def index(request):
    """Home page for Davy tyres"""
    context = {}
    tyre_form = TyreForm()
    context['tyre_form'] = tyre_form
    return render(request, "index.html", context)


def format_price_range(data):
    if not data.get('price'):
        return
    data['price__min_price'], data['price__max_price'] = data.get('price', '').split('-')
    data.pop('price', '')


def tyre_search(request):
    context, tyre_form = {}, TyreForm()

    non_empty = {key: value for key, value in request.POST.iteritems() if value and key != 'csrfmiddlewaretoken'}
    format_price_range(non_empty)
    results = Tyre.objects.filter(**non_empty)
    results_formatted = []
    for obj in results:
        results_formatted.append(dict((field.name, field.value_to_string(obj)) for field in obj._meta.fields))

    context['tyre_results'] = results_formatted
    context['tyre_form'] = tyre_form

    return render(request, "catalogue/tyre-results.html", context)


def about_us(request):
    return render(request, "davytyres/about-us.html",{})


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


def deals(request):
    return render(request, "davytyres/deals.html")

def tyre_categories(request):
   return render(request, "catalogue/tyre-categories.html", {})


def shock_shop(request):
    return render(request, "davytyres/shock-shop.html")

def auth_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if not user.is_active:
            return HttpResponseRedirect('/inactive/')
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin/')
    else:
        return HttpResponseRedirect('/logindenied/')
    # The login is authorised if its matches its value


def inactive(request):
    return render(request, 'registration/inactive.html')

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
        user.is_active = True
        user.save()
    except Exception as e:
        return render(request, 'unimplemented.html')
    return render(request, 'registration/activated.html')


def login(request):
    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def loggedin(request):
    context = {}
    return render(request, "registration/successful_login.html", context)


def logindenied(request):
    context = {'failed_login': True}
    return render(request, "registration/failed_login.html", context)


@csrf_exempt
def contact_us(request):
    context = {}
    if request.method == 'POST':
        message = "Enquirey from {} about tyres: {}".format(request.POST.get(''), request.POST.get('comments'))
        send_mail('tyre enquiry', message, 'enquireys@davytyres.co.nz', [settings.EMAIL_HOST_USER])
        context['name'] = request.POST.get('first_name')
        context['submitted'] = True
    return render(request, "davytyres/contact.html", context)
