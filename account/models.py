from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.CharField(max_length=20,unique=True,primary_key=True)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    mobile_no = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=10)