from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response


def index(request):
    """Home page for Davy tyres"""
    return render_to_response("index.html")


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


def login(request):
    context = {}
    return render(request, 'login.html', context)


def loggedin(request):
    context = {}
    return render(request, "succesful_login.html", context)


def logindenied(request):
    context = {}
    return render(request, "failed_login.html", context)

