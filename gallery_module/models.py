from django.db import models
from django_resized import ResizedImageField

class Gallery(models.Model):
    title = models.CharField(max_length=250, verbose_name="نام عکس")
    image = ResizedImageField(upload_to="gallery", verbose_name="عکس", quality=100, size=[350, 300], crop=['middle', 'center'])
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"