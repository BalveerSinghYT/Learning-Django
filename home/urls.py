from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registeration, name="register")
]

admin.site.index_title = "SAS Admin"