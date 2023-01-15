from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Resturants, Elements, OrdersElements, Orders, Votes
import time

# Create your views here.

# when a request comes to ask for index html return the render


# when a request comes to ask for about html return the render
def about(request):
    return render(request, 'about.html')

def restaurants(request):
    form = forms.AddRestaurantForm()
    if request.method == "POST":
        print(request.FILES)
        form = forms.AddRestaurantForm(request.POST, request.FILES)

        if form.is_valid():
            messages.success(request, "Data is valid")
            form.save()

            messages.success(request, "Restaurant Saved")

            return redirect("restaurants")
        else:
            messages.error(request, "Enter a valid data")

    try:
        restaurants_objs = Resturants.objects.all()
        # total_votes = Votes.objects.filter(user=request.user,restaurant=restaurants_objs)
        context = {"form": form, "restaurants": restaurants_objs,
                   "len_restaurants": len(restaurants_objs)}

    except:
        messages.error(request, "couldn't get restaurants")
        context = {"form": form}

    return render(request, "restaurants.html", context)


def orders(request):
    print("Order Started")
    if request.method == "POST":
        print(list(request.POST.items()))
        restaurant_id = request.POST.get("restaurant")
        print(f"Restaurant id:{restaurant_id}")
        restaurant = Resturants.objects.get(id=restaurant_id)
        # create an order
        try:
            order = Orders.objects.create(
                resturant=restaurant)

        except:
            pass

    context = {}
    return render(request, 'orders.html', context)


def menu(request, pk):
    restaurant = Resturants.objects.get(id=pk)

    items = Elements.objects.filter(resturant=restaurant)

    print(f"items: {items}")
    print(f"type of items: {type(items)}")
    form = forms.AddItemsForm()
    if request.method == 'POST':
        try:
            item = Elements.objects.create(
                name=request.POST.get('name'),
                price=request.POST.get('price'),
                resturant=restaurant
            )
            messages.success(request, "Item saved")
            return redirect("menu", pk=pk)
        except:
            messages.error(request, "Couldn't save the item")

    context = {'restaurant': restaurant, "form": form, "items": items}
    return render(request, "menu.html", context)


def cart(request, pk):

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
