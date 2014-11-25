from django.contrib.auth import authenticate, login 
from django.shortcuts import render
from django.views.generic import *
from app.forms import LoginForm
from app.models import *
# Create your views here.

class indexView(TemplateView):
	template_name = 'index.html'

class homeView(TemplateView):
	template_name = 'home.html'

class  LoginView(FormView):
	form_class = LoginForm
	template_name = 'login.html'
	success_url = '/garage/'

	def form_valid(self, form):
		login(self.request, form.user_cache)
		return super(LoginView, self).form_valid(form)

class GarageView(ListView):
	template_name = 'garage.html'
	model = VEHICULOS
