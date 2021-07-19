from django.db import models
from django.contrib.auth.models import User
# Create your models here.

nature = [("Doctor","Doctor"),("Patient","Patient")]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=nature, default="")
    line1 = models.CharField(max_length=255,default="")
    city = models.CharField(max_length=255,default="")
    pincode = models.IntegerField(default=0)
    state = models.CharField(max_length=255,default="")
    profile_pic= models.ImageField(upload_to="profile_pic",default="")

    def __str__(self):
        return self.user.username
