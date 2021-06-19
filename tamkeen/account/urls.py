from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.urls import include, path, re_path
from django.contrib.auth import views as auth_veiw 

from . import views 


app_name = "account"
urlpatterns = [
    path('logout', views.logout_view, name="logout"),
    path('changepw', auth_veiw.PasswordChangeView.as_view(success_url=reverse_lazy('books:Home')), name="changepw"),
    path('login', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('New_register/', views.register2, name="register2"),
    path('userlogin', auth_veiw.LoginView.as_view(), name="userlogin"),
    path('password_change/done/',auth_veiw.PasswordChangeDoneView.as_view(), name="password_change_complete"),

    path('password_reset/', auth_veiw.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_veiw.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_veiw.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_veiw.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
# aA@110110
