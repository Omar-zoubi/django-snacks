from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class firstView(TemplateView):
    template_name = 'home.html'

class secondView(TemplateView):
    template_name = 'about.html'
