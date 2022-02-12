import email
from django.db import models
from django.contrib.auth.models import User
from projects.models import Project, Issue, Comment


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    username = models.CharField(max_length=50, blank=False, default='Username')
    email = models.EmailField(max_length=100, blank=False, default='Email')
