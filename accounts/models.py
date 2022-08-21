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
