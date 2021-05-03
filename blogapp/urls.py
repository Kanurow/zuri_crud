from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'blogapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:post>/', views.post_single, name='post_single'),

]
