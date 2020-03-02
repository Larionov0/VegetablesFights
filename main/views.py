from django.shortcuts import render, redirect
from .models import *


def only_auth(view):  # decorator
    def new_view(request):
        if not request.user.is_authenticated:
            return redirect('authsys:log_in')
        return view(request)
    return new_view


def index(request):
    context = {
        "name": "Alan"
    }
    return render(
        request,
        'index.html',
        context
    )


@only_auth
def my_cab(request):
    context = {
        "user": request.user,
        "userprofile": request.user.userprofile
    }

    return render(
        request,
        "my_cab.html",
        context=context
    )


@only_auth
def deck_choosing(request):
    context = {
        "user": request.user,
        "userprofile": request.user.userprofile
    }

    return render(
        request,
        "deck_choosing.html",
        context=context
    )

