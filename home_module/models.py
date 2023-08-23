from django.db import models

from account_module.models import User

class AskQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    question = models.CharField(max_length=250, verbose_name="سوال")
    answer = models.TextField(verbose_name="پاسخ سوال")

    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوالات متداول"

    def __str__(self):
        return self.question