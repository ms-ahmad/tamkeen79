from django.urls import include, path, re_path


from . import views


app_name="books"
urlpatterns = [
    path('', views.Home, name="Home"),
    path('listbooks', views.ShowBooks, name="listbooks"),
    path('detail/<int:pk>', views.Detail, name="Detail"),
    path('l/', views.book_list, name="book_list"),
    path('<int:pk>/', views.book_store, name="book_store"),
    # re_path(r'(?P<slug>[-\w]+)/',views.book_store, name="book_store2"),


]
