from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView
from users.models import Users

from users.forms import SignUpForm



class SignUpView(CreateView):
    template_name ='Sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

class UserLoginView(LoginView):
    template_name = 'Login.html'

class UserLogoutView(ListView):
    model = Users
    template_name: str = 'Logout.html'


