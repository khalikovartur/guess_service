from django.urls import path
from . import views

app_name = 'guess'

urlpatterns = [
    path('', views.make_guess, name='make_guess')
]
