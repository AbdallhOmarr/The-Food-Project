## APP (polls)

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('menu/<int:pk>/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.register, name='register'),
    path('wahati/', views.wahati, name='wahati'),
    path('orders/', views.orders, name='orders'),

]
