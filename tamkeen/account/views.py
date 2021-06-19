from django.core.mail import EmailMessage
from django.contrib.auth.models import User
# from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView

from .forms import user_registertion_form ,customRegisterForm




# Create your views here.
def logout_view(request):
    logout(request)
  

    return redirect ('/')



def login(request):
    if request.method == "POST" and 'username' in request.POST and 'password' in request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("books:Home")

    return redirect("account:userlogin")






def register(request):
    if request.method == 'POST':
       user_form = user_registertion_form(request.POST)
       if user_form.is_valid():
           cd = user_form.cleaned_data
           new_user = user_form.save(commit=False)
           new_user.set_password(user_form.cleaned_data['password'])           
           new_user.save()
     
           return render(request, 'registration/register_done.html', {'new_user': new_user})
        #    return HttpResponse('register done')

    else:
       user_form = user_registertion_form()

    return render(request, 'registration/register.html', {"user_form": user_form})


def register2(response):
    if response.method == "POST":
        form = customRegisterForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = customRegisterForm()
    return render(response, "signup.html", {'form': form,})
