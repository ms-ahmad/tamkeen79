from django.urls import include, path, re_path

from . import views 


app_name = "account"
urlpatterns = [
    path('logout', views.logout_view, name="logout"),
    path('login', views.login, name="login"),
]
