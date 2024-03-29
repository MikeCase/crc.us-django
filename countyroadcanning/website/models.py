# import django
from django.db import models

# Create your models here.

class BlogPost(models.Model):

    title = models.CharField(max_length=125)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    name = models.CharField(max_length=25)
    comment = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

