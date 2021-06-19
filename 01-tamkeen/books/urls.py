from django.urls import  path, re_path


from . import views


app_name = "books"
urlpatterns = [
    path('', views.Home, name="Home"),
    path('listbooks', views.ShowBooks, name="listbooks"),
    path('detail/<int:pk>', views.Detail, name="Detail"),
    path('l/', views.book_list, name="book_list"),
    path('publisher/<int:pk>/', views.books_Publisher, name="books_Publisher"),
    path('category/<int:pk>/', views.books_category, name="books_category"),
    path('author/<int:pk>/', views.books_author, name="books_author"),
    # path('partial/nav.html', views.nav, name="nav"),

    # re_path(r'(?P<slug>[-\w]+)/',views.book_store, name="book_store2"),


]
