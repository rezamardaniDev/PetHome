# Generated by Django 4.2.3 on 2023-08-26 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0005_alter_ordercheckout_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercheckout',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_module.order', verbose_name='رسید'),
        ),
    ]
