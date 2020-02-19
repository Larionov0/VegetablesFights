from django.shortcuts import render, redirect
from django.contrib import auth
from .models import *


def log_in(request):
    context = {}
    if request.POST:
        POST = request.POST
        username = POST.get("username", '')
        password = POST.get("password", '')
        user = auth.authenticate(username=username, password=password)
        if user is None:
            context['error'] = 'Incorrect username or password!!!'
            return render(
                request,
                'log_in_page.html',
                context
            )
        else:
            auth.login(request, user)
            try:
                user.userprofile
            except:
                UserProfile.objects.create(user=user)

            return redirect('main:my_cab')

    else:
        return render(
            request,
            'log_in_page.html',
            context
        )


def log_out(request):
    auth.logout(request)
    return redirect('authsys:log_in')
