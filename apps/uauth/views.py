from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm ,UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import (
	authenticate,

	login,
	logout,
	)

@login_required
def homepage(request):
	return render(request, 'pages/index.html')



def login_view(request):
	next = request.POST.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		password2 = form.cleaned_data.get('password2')
		print(password2)
		user = authenticate(username=username, password=password)
		login(request,user)
		if next:
			return redirect(next)
		return redirect('home')

	context = {
	"form":form
	}
	return render(request,'uauth/login.html',context)


def register_view(request):
	next = request.POST.get('next')
	form = UserRegisterForm(request.POST or None)
	context = {
        "form":form
    }
	if form.is_valid():
		username = form.cleaned_data.get("username",False)
		email = form.cleaned_data.get("email",False)
		password = form.cleaned_data.get("password")
		user = User.objects.create_user(username=username,email=email,password=password)
		user.save()
		if next:
			return redirect(next)
		return redirect('home')
		
	return render(request,"uauth/register.html",context)
	

def logout_view(request):
	logout(request)
	return redirect('home')
    






