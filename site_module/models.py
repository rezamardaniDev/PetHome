from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=250, verbose_name="عنوان سایت")
    site_url = models.CharField(max_length=250, verbose_name="دامنه سایت")
    about_us = models.TextField(verbose_name="متن درباره ما")
    contact_us_text = models.CharField(max_length=250,verbose_name="متن تماس با ما")
    address = models.CharField(max_length=250, verbose_name="آدرس ما", null=True)
    phone = models.CharField(max_length=250, verbose_name="تلفن تماس", null=True)
    email = models.CharField(max_length=250, verbose_name="ایمیل", null=True)
    info = models.TextField(verbose_name="درباره شرکت", null=True)
    copy_right = models.CharField(max_length=255, verbose_name="متن کپی رایت")
    is_main_setting = models.BooleanField(verbose_name="تنظیمات اصلی")
    social_instagram = models.CharField(max_length=250, verbose_name="اینستاگرام", null=True, blank=True)
    social_telegram = models.CharField(max_length=250, verbose_name="تلگرام", null=True, blank=True)
    social_whatsapp = models.CharField(max_length=250, verbose_name="واتس آپ", null=True, blank=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "تنظیمات"