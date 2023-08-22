from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name="تلفن همراه")
    email_active_code = models.CharField(max_length=100, verbose_name="کد فعالسازی")
    address = models.CharField(max_length=250, verbose_name="آدرس", default="ثبت نشده", blank=True)
    profile_image = ResizedImageField(upload_to="user_profile", size=[80 , 80], crop=['middle', 'center'],quality=100, blank=True)


    def delete(self, *args, **kwargs):
            storage, path = self.image.storage, self.image.path
            storage.delete(path)
            super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural="کاربران"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"