from django.shortcuts import render


def log_in(request):
    context = {}
    return render(
        request,
        'log_in_page.html',
        context
    )


def log_out(request):
    pass
