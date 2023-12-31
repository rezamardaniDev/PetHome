# Generated by Django 4.2.3 on 2023-08-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=250, verbose_name='موضوع')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ دریافت')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
            },
        ),
    ]
