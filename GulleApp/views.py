from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserSignup, UserLogin, UserForm
from django.contrib import messages
from .models import (Message,)
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import JsonResponse

# def home(request):
# 	return render(request, 'home.html')

class Signup(View):
	form_class = UserSignup
	template_name = 'signup.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			messages.success(request, "You have successfully signed up.")
			login(request, user)
			return redirect("home")
		messages.warning(request, form.errors)
		return redirect("signup")


class Login(View):
	form_class = UserLogin
	template_name = 'login.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				messages.success(request, "Welcome Back! " +request.user.username)
				return redirect('home') 
			messages.warning(request, "Wrong email/password combination. Please try again.")
			return redirect("login")
		messages.warning(request, form.errors)
		return redirect("login")


class Logout(View):
	def get(self, request, *args, **kwargs):
		logout(request)
		messages.success(request, "You have successfully logged out.")
		return redirect("login")

def no_access(request):
	return render(request, 'no_access.html')

#####################


def profile(request, user_id):
	user = User.objects.get(id=user_id)
	messages = Message.objects.filter(teacher= user)
	context = {
		"user": user,
		"messages": messages,
	}

	return render(request, 'profile.html', context)


def professors_list(request):
	professors = User.objects.all()

	if request.GET.get('q'):
		q = request.GET.get('q')
		query = Q(username__contains=q)|Q(first_name__contains=q)|Q(last_name__contains=q)
		professors = User.objects.filter(query)

	context = {
		"professors" : professors
	}

	return render(request, 'home.html', context)


