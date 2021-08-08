from django.db import models
from django.utils import timezone 
from users.models import Profile

# Create your models here.
class MyAnimations(models.Model):
    def __str__(self):
        return self.animation_name

    animation_user=models.ForeignKey(Profile,default=1, on_delete=models.CASCADE)
    animation_name=models.CharField(max_length=200)
    animation_details=models.TextField(max_length=500,blank=True,null=True,default='N/A')
    animation_rating=models.FloatField(default=0)
    animation_createdate= models.DateField('date created at',blank=True,null=True)
    animation_image= models.ImageField(upload_to='images/',default="images/None/Noimg.jpg")