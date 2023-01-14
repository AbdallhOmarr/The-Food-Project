from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_orders_data),
    path('getOrders', views.get_orders_data, name="ordersData"),
    path('getRestaurants', views.get_restaurants_data, name="restaurantsData"),
    path('addVotes', views.add_votes, name="votePOST"),
    path('getVotes', views.get_votes_data, name="voteGET"),

]
