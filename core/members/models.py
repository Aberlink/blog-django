from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/profiles/")
    
    def __str__(self) -> str:
        return str(self.user)
