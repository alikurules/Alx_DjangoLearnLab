from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from taggit.managers import TaggableManager



class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    # Reference to the User model to track the author of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()  # Add tagging functionality

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"