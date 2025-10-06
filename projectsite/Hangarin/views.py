from django.shortcuts import render

from django.views.generic.list import ListView
from Hangarin.models import Priority

class HomePageView(ListView):
    model = Priority
    context_object_name = 'home'
    template_name = "home.html"

