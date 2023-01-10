from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
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

    context = {'form': form}
    return render(request, "register.html", context)


def wahati(request):
    return render(request, "wahati.html")