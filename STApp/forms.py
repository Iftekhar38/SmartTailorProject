from django import forms
from STApp.models import GalaryModel
from django.contrib.auth.models import User

class addProductForm(forms.ModelForm):
    class Meta:
        model = GalaryModel
        fields = '__all__'
        
class signUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        