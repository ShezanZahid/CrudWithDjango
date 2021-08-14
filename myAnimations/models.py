from django.db import models
from django.utils import timezone 
from users.models import Profile
from django.contrib.auth.models import User

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
    status_type=models.TextChoices('status_type','Approved Pending Rejected')
    status=models.CharField(default="Pending",choices=status_type.choices, max_length=100)
    likes= models.ManyToManyField(User,related_name='post_user',default=None,blank=True)
    like_count = models.BigIntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(MyAnimations,on_delete=models.CASCADE,related_name='comment_post')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user')
    content = models.TextField()
    publish= models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta :
        ordering = ('publish',)

    def __str__(self):
        return f"Commented by {self.user} at {self.publish}"
