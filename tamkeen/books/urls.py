from django.urls import include, path

from . import views


app_name="books"
urlpatterns = [
    path('listbooks', views.ShowBooks, name="listbooks"),
    path('detail/<int:pk>', views.Detail, name="Detail"),


]
