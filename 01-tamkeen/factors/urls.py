from django.urls import include, path, re_path


from . import views


app_name = "factors"
urlpatterns = [
    path('Add_to_cart/<int:pk>', views.Add_to_cart, name="Add_to_cart"),
    
]
