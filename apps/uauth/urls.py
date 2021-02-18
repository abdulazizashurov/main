from django.urls import path
from .views import (
	homepage,
	login_view,
	register_view,
	logout_view
	)

urlpatterns =[
	path('' , homepage , name='home'),
	path('accounts/login/' , login_view , name='login'),
	path('accounts/register/' ,register_view , name='register'),
	path('accounts/logout/' ,logout_view , name='logout'),


]