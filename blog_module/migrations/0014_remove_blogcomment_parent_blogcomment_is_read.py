# Generated by Django 4.2.3 on 2023-08-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0013_blogcomment_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='خوانده شده'),
        ),
    ]
