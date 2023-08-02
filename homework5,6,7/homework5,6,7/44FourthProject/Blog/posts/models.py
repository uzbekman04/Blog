from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    posted_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        reverse_lazy('home')

    def __str__(self):
        return self.title
