from django.shortcuts import render

from django.views.generic import ListView
from users.models import Users



class Sign_Up_View(ListView):
    model = Users
    template_name: str = 'sign_up.html'


