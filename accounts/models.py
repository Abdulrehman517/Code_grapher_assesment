import binascii
import os

from django.contrib.auth.models import AbstractUser
from django.db import models
import holidays


class User(AbstractUser):
    holiday = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.holiday:
            date_joined = self.date_joined
            for day in holidays.US(years=2022).items():
                day_name = day[1]
                date_of_day = day[0]
                if date_joined == date_of_day:
                    self.holiday = day_name
                else:
                    pass
        return super().save(*args, **kwargs)


class Token(models.Model):
    user = models.OneToOneField(User, related_name='auth_token', on_delete=models.CASCADE)
    key = models.CharField(max_length=40, primary_key=True)
    created = models.DateTimeField(auto_now_add=True, null=True , blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key