from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
        
class Workshop(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name