from django.db import models

class ContactUs(models.Model):
    email = models.EmailField(max_length=250, verbose_name="ایمیل")
    subject = models.CharField(max_length=250, verbose_name="موضوع")
    message = models.TextField(verbose_name="متن پیام")
    date = models.DateTimeField(verbose_name="تاریخ دریافت",auto_now_add=True)

    class Meta:
        verbose_name  = "پیام"
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return self.subject
