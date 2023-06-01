from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django import forms
from .models import Myblog


class Myform(UserCreationForm):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                #  'Email':forms.EmailInput(attrs={'class':'form-control'}),
                 'username':forms.TextInput(attrs={'class':'form-control'})}
        
class userlogin(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))   
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))   


class addform(forms.ModelForm):

    class Meta:
     model=Myblog
     fields=['title','con']
     labels={'con':'content'}
     widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
     'con':forms.Textarea(attrs={'class':'form-control'})}