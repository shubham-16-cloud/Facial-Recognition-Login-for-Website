from django.db import models
from datetime import datetime

# Create your models here.
class banner(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    subtext = models.CharField(max_length=1000)
    image = models.ImageField()
    dateofinsert = models.DateField()
    def __str__(self):
        return self.title

class events(models.Model):
    id = models.AutoField(primary_key=True)
    event_date = models.DateField()
    event_title = models.CharField(max_length=1000)
    event_text = models.CharField(max_length=1000)
    event_img = models.ImageField(upload_to='event/')
    def __str__(self):
        return self.event_title

class news(models.Model):
    id = models.AutoField(primary_key=True)
    news_date = models.DateField()
    news_title = models.CharField(max_length=1000)
    news_text = models.CharField(max_length=1000)
    news_img = models.ImageField(upload_to='news/')
    def __str__(self):
        return self.news_title

class about(models.Model):
    id = models.AutoField(primary_key=True)
    ab_title = models.CharField(max_length=50)
    ab_subtext = models.CharField(max_length=1000)
    ab_img = models.ImageField(upload_to='about/')
    def __str__(self):
        return self.ab_title