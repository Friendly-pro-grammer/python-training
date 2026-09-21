from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    is_published=models.BooleanField()
    
    def __str__(self):
        return self.name
     