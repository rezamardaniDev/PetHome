from django.db import models
from account_module.models import User
from product_module.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    is_paid = models.BooleanField(verbose_name="پرداخت شده / پرداخت نشده")
    payment_date = models.DateField(null=True, blank=True, verbose_name="تاریخ پرداخت")
    total_amount = models.IntegerField(default=0, blank=True, verbose_name="مجموع")

    def __str__(self):
        return str(self.id)

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count

        return total_amount

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبدهای خرید کابران"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="سبد خرید")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    final_price = models.IntegerField(null=True, blank=True, verbose_name="قیمت نهایی تکی محصول")
    count = models.IntegerField(verbose_name="تعداد")

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = "جزئیات سبد خرید"
        verbose_name_plural = "لیست جزئیات سبدهای خرید"


class OrderCheckout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='رسید')
    first_name = models.CharField(max_length=250, verbose_name='نام')
    last_name = models.CharField(max_length=250, verbose_name='نام خانوادگی')
    state = models.CharField(max_length=250, verbose_name='استان')
    city = models.CharField(max_length=250, verbose_name='شهر')
    street = models.CharField(max_length=250, verbose_name='خیابان')
    apartment = models.CharField(max_length=250, verbose_name='آپارتمان')
    zipcode = models.CharField(max_length=250, verbose_name='کد پستی')
    phone = models.CharField(max_length=250, verbose_name='شماره تماس')
    sended = models.BooleanField(verbose_name='ارسال شده / نشده')

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'


class Discount(models.Model):
    code = models.CharField(max_length=250, null=True, unique=True, verbose_name="کد تخفیف")
    percent = models.IntegerField(null=True, verbose_name="درصد تخفیف")
    status = models.BooleanField(default=True, verbose_name="وضعیت")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کدهای تخفیف"


class UserDescount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    code = models.CharField(max_length=250, verbose_name="کد")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'کد استفاده شده'
        verbose_name_plural = "کدهای استفاده شده"
