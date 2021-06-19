from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField , UserCreationForm
from django.contrib.auth.models import User
# from .models import User


# class CustomAuthenticationForm(AuthenticationForm):
#     email = forms.EmailField(label='البريد الالكتروني', required=False)
#     username = UsernameField(
#         label='اسم المستخدم',
#         widget=forms.TextInput(
#             attrs={'autofocus': True, 'class': 'form-control ', })
#     )


class customRegisterForm(UserCreationForm):
    email = forms.EmailField(label='البريد الالكتروني', required=True)

      
    class Meta:
        model =User
        fields = ('username', 'email','first_name', 'last_name',)
        # fields = '__all__'



class user_registertion_form(forms.ModelForm):
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput, required=True)
    # avatar = forms.ImageField( required=False)
    # password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput, required=True)


    class Meta:
        model =User
        fields = ('username', 'first_name', 'last_name', )
        # fields = '__all__'



    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور وتأكيد كلمة المرور غير متطابقة')

        return cd['password2']
