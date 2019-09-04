from django.db import models

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length = 30,unique = True)
  password = models.TextField()

class Post(models.Model):
  creator = models.CharField(max_length = 30)
  content = models.TextField()
  created_at = models.DateTimeField("date published")
