from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import auth


# Create your views here.
def logout_view(request):
    logout(request)
  

    return redirect ('/')



def login(request):
    if request.method == "POST" and 'username' in request.POST and 'password' in request.POST:
        username = request.POST["username"]
        password =request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("books:Home")
    
    return redirect("books:Home")
