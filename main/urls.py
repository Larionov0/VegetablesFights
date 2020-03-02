from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('my_cab', views.my_cab, name='my_cab'),
    path('battle', views.deck_choosing, name='deck_choosing')
]
