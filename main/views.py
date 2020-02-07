from django.shortcuts import render


def index(request):
    context = {
        "name": "Alan"
    }
    return render(
        request,
        'index.html',
        context
    )
