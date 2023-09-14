from django.db import models
from django_jalali.db import models as jmodels

from account_module.models import User


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
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name="دسته بندی")
    image = models.ImageField(upload_to="blog", verbose_name="عکس", null=True)
    short_description = models.CharField(max_length=250, verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name='متن')
    created_date = jmodels.jDateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    slug = models.SlugField(max_length=250, allow_unicode=True, verbose_name="اسلاگ", db_index=True, null=True,
                            blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        storage.delete(path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class BlogComment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="پست", related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    message = models.TextField(verbose_name="متن نظر")
    response = models.TextField(verbose_name="پاسخ ادمین", null=True, blank=True)
    is_read = models.BooleanField(verbose_name="خوانده شده", default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


class BlogVisit(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="پست", related_name="post_visit")
    ip = models.CharField(max_length=30, verbose_name="آی پی کاربر")
    user = models.ForeignKey(User, null=True, blank=True, verbose_name="کاربر مشاهده کرده", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} / {self.ip}'

    class Meta:
        verbose_name = "بازدید پست"
        verbose_name_plural = "بازدید های پست"
