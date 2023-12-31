# Generated by Django 4.2.3 on 2023-08-20 06:00

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0004_remove_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['center', 'center'], force_format=None, keep_meta=True, quality=-1, scale=None, size=[80, 80], upload_to='user_profile'),
        ),
    ]
