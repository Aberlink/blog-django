from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=25, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publicated = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} | {str(self.author)}'
    
    def get_absolute_url(self):
        return reverse('article_detail', args=(str(self.id)))
