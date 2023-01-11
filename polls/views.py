from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

# when a request comes to ask for index html return the render


def index(request):
    return render(request, 'index.html')


# when a request comes to ask for about html return the render
def about(request):
    return render(request, 'about.html')


def restaurants(request):
    return render(request, "restaurants.html")


def orders(request):
    return render(request, "orders.html")


def cart(request):
    return render(request, "cart.html")


def login(request):
    return render(request, "login.html")


def register(request):

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # login(request,user)
            redirect('index')
        else:
            pass
            # messages.error(request, "An Error occured during registeration!")
    context = {'form': form}
    return render(request, "register.html", context)


def wahati(request):
    return render(request, "wahati.html")
