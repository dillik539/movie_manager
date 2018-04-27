from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length = 20, unique = True, blank = False)
    firstname = models.CharField(max_length = 200, blank = False)
    lastname = models.CharField(max_length = 200, blank = False)
    email = models.CharField(max_length = 200, unique = True,blank = False)
    password1 = models.CharField(max_length = 200, blank = False)
    password2 = models.CharField(max_length = 200, blank = False)
