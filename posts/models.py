from django.db import models

# Create your models here.
from accounts.models import User


class Posts(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.CharField(max_length=700, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')


    def __str__(self):
        return self.title