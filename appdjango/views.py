from django.shortcuts import render, render_to_response
from appdjango.models import UserProfile
import datetime

# Create your views here.


def home(request):
	return render(request, 'home.html')

def index(request):
	name = request.POST.get('user')
	email = request.POST.get('email')
	password = request.POST.get('password')
	obj = UserProfile(
		user_name = name,
		email_id = email,
		password = password)
	obj.save()
	return render(request, 'index.html',{'name':name, 'email':email, 'password':password})


# def show(request):
# 	obj = UserProfile.objects.all()
# 	return render(request, 'show.html', {'obj':obj})