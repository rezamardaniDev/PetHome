# Generated by Django 4.2.3 on 2023-08-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0005_alter_blog_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='view',
            field=models.IntegerField(blank=True, default=0, verbose_name='تعداد بازدید'),
        ),
    ]
