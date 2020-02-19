from django.shortcuts import render, redirect


def index(request):
    context = {
        "name": "Alan"
    }
    return render(
        request,
        'index.html',
        context
    )


def my_cab(request):
    if not request.user.is_authenticated:
        return redirect('authsys:log_in')
    pass
