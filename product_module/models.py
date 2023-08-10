from django.db import models
from django.utils.text import slugify


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
    productcategory = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="دسته بندی")

    price = models.IntegerField(verbose_name="قیمت", null=True)
    count = models.IntegerField(verbose_name="تعداد")
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")
    slug = models.SlugField(verbose_name="اسلاگ", default="", null=False, blank=True, db_index=True, unique=True)
    image = models.ImageField(upload_to="product_image", verbose_name="عکس محصول", null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.productcategory.url_title}-{self.name}")
        super().save(*args, **kwargs)

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
