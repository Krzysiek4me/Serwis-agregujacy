from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Events
from typing import Any, Dict


class Index(ListView):
    model = Events
    template_name: str = 'base.html'

