from django.db import models

from account_module.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان")
    url_title = models.SlugField(max_length=250, verbose_name="عنوان در url", null=True)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="نام")
    description = models.TextField(verbose_name="توضیحات")
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="دسته بندی")

    price = models.IntegerField(verbose_name="قیمت", null=True)
    count = models.IntegerField(verbose_name="تعداد")
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")
    slug = models.SlugField(verbose_name="اسلاگ", null=False, blank=True, db_index=True)
    image = models.ImageField(upload_to="product_image", verbose_name="عکس محصول", null=True)


    def delete(self, *args, **kwargs):
            storage, path = self.image.storage, self.image.path
            storage.delete(path)
            super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["price"]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول", related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر", related_name='users')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    message = models.TextField(verbose_name="متن نظر")
    response = models.TextField(verbose_name="پاسخ ادمین", null=True, blank=True)
    is_read = models.BooleanField(verbose_name="خوانده شده", default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"