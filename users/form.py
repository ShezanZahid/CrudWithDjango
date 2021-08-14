from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Information a valid email address.')
    class Meta:
        model = User
        fields=['username','email','first_name','last_name','password1','password2',]

class ProfileForm(forms.ModelForm): 
    class Meta:
        model=Profile
        fields=['user','occupation','address','dob','hobbies','image',]
        widgets = {
            'address': forms.Textarea(attrs={'cols': 40, 'rows': 10},),
        }
       
