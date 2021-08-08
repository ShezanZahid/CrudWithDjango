from django import forms
from django.db import models
from .models import MyAnimations


class MyAnimationCreateForm(forms.ModelForm):
    class Meta:
        model=MyAnimations
        animation_createdate = forms.DateTimeField(required=False)

        fields=['animation_name','animation_details','animation_rating','animation_createdate','animation_image']
        widgets = {
            'animation_details': forms.Textarea(attrs={'cols': 40, 'rows': 10},),
            'animation_name':forms.TextInput(attrs={'class': 'from-group'}),
            'animation_createdate': forms.DateInput(attrs={'type': 'date'})
        }