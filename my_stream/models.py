from django.db import models

# Create your models here.


class User(models.Model):
    username= models.CharField(max_length=100, unique=False)
    email= models.EmailField(default="youssef@gmail.com",unique=True)


class Media(models.Model):
    name_image= models.CharField(max_length=100)
    image=models.ImageField(upload_to='upload_image/')

class Video(models.Model):
    name_video= models.CharField(max_length=100)
    Video = models.FileField(upload_to='upload_video/')