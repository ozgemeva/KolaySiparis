from django.shortcuts import render
from KolaySiparisApp.models import UserInfo
from django.contrib.auth.models import User
from .forms import RegisterForm
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
     if request.method == 'POST':
         # create a form instance and populate it with data from the request:
         form = LoginForm(request.POST)

         # check whether it's valid:
         if form.is_valid():
             print "buraya geldim"
             user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
             login(request,user)
             return HttpResponseRedirect('/')

         else:
             print form.errors
             print "form valid degil"

     # if a GET (or any other method) we'll create a blank form
     else:
         print "else geldim"
         print request.method
         form = LoginForm()

     print "buraya geldim"
     return render(request, 'home.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'logout_view.html')


def register(request):
      # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)

        # check whether it's valid:
        if form.is_valid() and len(form.cleaned_data) >=9:
            print "burdayim"
            print "form valid"
            u = User.objects.create_user(username=form.cleaned_data["username"],email=form.cleaned_data["email"],password= form.cleaned_data["password"] )
            u.is_superuser = False
            u.last_name = form.cleaned_data["lastname"]
            u.first_name = form.cleaned_data["firstname"]
            u.save()
            userinf = UserInfo()
            userinf.user = u
            userinf.adress = form.cleaned_data["adress"]
            userinf.location = form.cleaned_data["city"] + "/" + form.cleaned_data["state"]
            userinf.phone = form.cleaned_data["phone"]

            userinf.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            login(request,user)
            return HttpResponseRedirect('/login/')

        else:
            print form.errors
            print "form valid degil"

    # if a GET (or any other method) we'll create a blank form
    else:
        print "else geldim"
        print request.method
        form = RegisterForm()

    print "buraya geldim"
    return render(request, 'register.html', {'form': form})


def restaurant_login_view(request):
    return render(request, 'restaurant_login.html')


def login_view(request):
    return render(request, 'login_view.html')

def customerRestaurant_view(request):
    return render(request,'customerRestaurant.html')
