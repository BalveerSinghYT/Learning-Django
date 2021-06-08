from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.Registeration, name="register"),
    path('base', views.base, name="base"),
    path('records', views.records, name="records"),
    path('attendance', views.attendance_data, name="attendance_data"),
    # path('livefeed', views.livefeed, name="livefeed"),
    # path('feed', views.feed, name="feed"),

]

admin.site.index_title = "SAS Admin"