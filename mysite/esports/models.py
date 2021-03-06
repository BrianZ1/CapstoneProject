from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    comment = models.TextField()
    
    def __str__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=50)
    game = models.CharField(max_length=50)
    count = models.IntegerField()
    
    def increment_count(self):
        self.count += 1
    
class Event(models.Model):
    name = models.CharField(max_length=50)
    game = models.CharField(max_length=50)
    count = models.IntegerField()
    
    def increment_count(self):
        self.count += 1