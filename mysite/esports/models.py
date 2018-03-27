from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    comment = models.TextField()
    
    def __str__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    count = models.IntegerField()
    
class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    count = models.IntegerField()