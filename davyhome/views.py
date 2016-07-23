from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from bookings.forms import RegistrationForm


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
    return render(request, "test/catalogue.html", context)


def unimplemented(request):
    return render(request, "unimplemented.html")


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
            user_form.save()
            return render(request, 'registration/register-success.html', context)

    return render(request, 'registration/registration_page.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def loggedin(request):
    context = {}
    return render(request, "registration/successful_login.html", context)


def logindenied(request):
    context = {'failed_login': True}
    return render(request, "registration/failed_login.html", context)

