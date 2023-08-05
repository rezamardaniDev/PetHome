from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان")
    url_title = models.SlugField(max_length=250 , verbose_name="عنوان در url" , null=True)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'



class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="نام")
    descrtiption = models.TextField(verbose_name="توضیحات")
    productcategory = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="دسته بندی")
    
    price = models.IntegerField(verbose_name="قیمت", null=True)
    count = models.IntegerField(verbose_name="تعداد")
    description = models.TextField(verbose_name="توضیحات")
    is_active = models.BooleanField(verbose_name="موجود / ناموجود")


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["price"]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

