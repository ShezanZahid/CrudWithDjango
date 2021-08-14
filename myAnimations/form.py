from django import forms
from django.db import models
from .models import Comment, MyAnimations


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
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        widgets = {
            'content': forms.Textarea(attrs={"class":"form-control",'cols': 100, 'rows': 7}),
        } 
        labels = {
            'content': 'Comment',
        }
