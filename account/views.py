from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('account:logout')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('account:login')
			

		context = {'form':form}
		return render(request, 'account/register.html', context)
def loginView(request):
	context = {
		'page_title':'LOGIN',
	}
	user = None
	if request.method == "POST":
		
		username_login = request.POST['username']
		password_login = request.POST['password']
		
		user = authenticate(request, username=username_login, password=password_login)

		if user is not None:
			login(request, user)
			return redirect('home:home')
		else:
			return redirect('account:login')
		
	return render(request,'account/login.html', context)

@login_required
def logoutView(request):
	context = {
		'page_title':'logout'
	}

	if request.method == "POST":
		if request.POST["logout"] == "Submit":
			logout(request)

		return redirect('home:home')	


	return render(request, 'account/logout.html', context)
# class loginView(TemplateView):
#     template_name = 'account/login.html'
#     extra_context = {
#         'Judul': 'Home',
#     }