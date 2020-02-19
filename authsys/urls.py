from django.urls import path
from .views import *

app_name = 'authsys'

urlpatterns = [
    path('log_in', log_in, name='log_in'),
    path('log_out', log_out, name='log_out')
]
