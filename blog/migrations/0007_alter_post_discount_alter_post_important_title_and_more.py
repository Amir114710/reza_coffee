# Generated by Django 4.0.3 on 2022-10-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='discount',
            field=models.IntegerField(null=True, verbose_name='قیمت تخفیف خورده'),
        ),
        migrations.AlterField(
            model_name='post',
            name='important_title',
            field=models.CharField(max_length=100, verbose_name='نام کالا به اینگلیسی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(null=True, verbose_name='قیمت اصلی'),
        ),
    ]