from django.db import models
from django.contrib.auth.models import User
from occupationType.models import OccupationType

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    occupation = models.ForeignKey(OccupationType,default=1, on_delete=models.CASCADE)
    address=models.TextField(max_length=500)
    dob=models.DateField()
    hobbyType=models.TextChoices('hobbyType','3D_Art 3D_Rendering 3D_Modeling Painting')
    hobbies=models.CharField(default="Select_a_Hobby",choices=hobbyType.choices, max_length=100)
    image=models.ImageField(upload_to='images/profpic',default="images/None/Noimg.jpg")

    def __str__(self):
        return self.user.username 

