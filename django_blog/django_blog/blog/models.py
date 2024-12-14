from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title           = models.CharField(max_length=200)
    content         = models.TextField()
    published_date  = models.DateTimeField(auto_now_add=True)
    # Reference to the User model to track the author of the post
    author          = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title


    
