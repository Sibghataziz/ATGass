from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# model for post
categories =[("Mental Health","Mental Health"),("Heart Disease","Heart Disease"),("Covid19","Covid19"),("Immunization","Immunization")]
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics', blank=True)
    category = models.CharField(max_length=255, choices=categories, default="")
    summary = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    draft = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title