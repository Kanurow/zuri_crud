from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('products/', views.products, name = 'products'),
    path('customer/', views.customer, name = 'customer'),
    path("register/", views.registerPage, name = 'register'),
    path("login/", views.loginPage),
    path("logout/", views.logout_user, name = 'logout'),

]