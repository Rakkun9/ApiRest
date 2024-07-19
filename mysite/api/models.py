from django.db import models

# Create your models here.

class BlogPost(models.Model): 
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.title
    
class User(models.Model):
    first  = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.first