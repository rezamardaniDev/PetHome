from django.db import models

# Create your models here.
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=250, verbose_name="عنوان سایت")
    site_url = models.CharField(max_length=250, verbose_name="دامنه سایت")
    about_us = models.TextField(verbose_name="متن درباره ما")
    address = models.CharField(max_length=250, verbose_name="آدرس ما", null=True)
    phone = models.CharField(max_length=250, verbose_name="تلفن تماس", null=True)
    email = models.CharField(max_length=250, verbose_name="ایمیل", null=True)
    copy_right = models.CharField(max_length=255, verbose_name="متن کپی رایت")
    site_logo = models.ImageField(upload_to="site-settings", verbose_name="لوگو سایت")
    is_main_setting = models.BooleanField(verbose_name="تنظیمات اصلی")

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "تنظیمات"