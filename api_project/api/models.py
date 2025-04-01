from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ Ensure this field exists
