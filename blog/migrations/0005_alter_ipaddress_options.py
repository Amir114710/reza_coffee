# Generated by Django 4.0.3 on 2022-10-04 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_ipaddress_post_hits'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipaddress',
            options={'verbose_name': 'ای پی', 'verbose_name_plural': 'ادرس ای پی'},
        ),
    ]
