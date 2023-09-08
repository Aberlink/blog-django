from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return str(self.name)

    @classmethod
    def get_default(cls):
        return cls.objects.get_or_create(name="uncatagorized")[0]


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=25, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=Category.get_default
    )
    body = models.TextField()
    publicated = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {str(self.author)}"

    def get_absolute_url(self):
        return reverse("article_detail", args=(self.id,))
