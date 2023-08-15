from django.db import models
from django_jalali.db import models as jmodels

from account_module.models import User


# Create your models here.
class BlogCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name="نام دسته بندی")
    url_title = models.CharField(max_length=250, verbose_name="عنوان در url", unique=True)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی مقالات"


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان مقاله")
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name="دسته بندی")
    image = models.ImageField(upload_to="blog", verbose_name="عکس", null=True)
    short_description = models.CharField(max_length=250 ,verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name='متن')
    created_date = jmodels.jDateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    view = models.IntegerField(verbose_name="تعداد بازدید", blank=True, default=1)
    slug = models.SlugField(max_length=250, allow_unicode=True,  verbose_name="اسلاگ", db_index=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class BlogComment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="پست")
    parent = models.ForeignKey('BlogComment',null=True, blank=True, on_delete=models.CASCADE, verbose_name="والد")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    message = models.TextField(verbose_name="متن نظر")

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"