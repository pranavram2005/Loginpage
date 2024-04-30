from django.db import models

class User1(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=255)
  username = models.CharField(max_length=255) 
  password = models.CharField(max_length=255) 
 