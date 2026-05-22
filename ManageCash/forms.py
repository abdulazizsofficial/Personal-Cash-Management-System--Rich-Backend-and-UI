from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from ManageCash.models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model=AuthUserModel
        fields=['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields='__all__'
        exclude=['user']
        
class CashForm(forms.ModelForm):
    class Meta:
        model=CashModel
        fields='__all__'
        exclude=['user']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=ExpenseModel
        fields='__all__'
        exclude=['user']