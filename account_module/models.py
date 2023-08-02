from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name="تلفن همراه")
    emal_active_code = models.CharField(max_length=100, verbose_name="کد فعالسازی")

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural="کاربران"

    def __str__(self):
        return self.first_name