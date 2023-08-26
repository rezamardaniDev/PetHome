# Generated by Django 4.2.3 on 2023-08-26 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, verbose_name='نام')),
                ('last_name', models.CharField(max_length=250, verbose_name='نام خانوادگی')),
                ('state', models.CharField(max_length=250, verbose_name='استان')),
                ('city', models.CharField(max_length=250, verbose_name='شهر')),
                ('street', models.CharField(max_length=250, verbose_name='خیابان')),
                ('apartment', models.CharField(max_length=250, verbose_name='آپارتمان')),
                ('zipcode', models.CharField(max_length=250, verbose_name='کد پستی')),
                ('phone', models.CharField(max_length=250, verbose_name='شماره تماس')),
                ('sended', models.BooleanField(verbose_name='ارسال شده / نشده')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_module.order', verbose_name='رسید')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
    ]
