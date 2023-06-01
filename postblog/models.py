from django.db import models

# Create your models here.
class Myblog(models.Model):
    title=models.CharField(max_length=100)
    con=models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    message=models.TextField(max_length=250)