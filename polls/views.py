from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# when a request comes to ask for index html return the render


# when a request comes to ask for about html return the render
def about(request):
    return render(request, 'about.html')


def restaurants(request):
    return render(request, "restaurants.html")


def orders(request):
    return render(request, "orders.html")


def cart(request):
    return render(request, "cart.html")


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Password is incorrect")

    context = {"key": "login"}
    return render(request, "login_register.html", context)


def logoutView(request):
    logout(request)
    return redirect("/")


def register(request):

    form = forms.UserCreateForm()
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            pass
            # messages.error(request, "An Error occured during registeration!")
    context = {'form': form, "key": "register"}
    return render(request, "login_register.html", context)


def wahati(request):
    return render(request, "wahati.html")


def index(request):
    return render(request, 'index.html')
