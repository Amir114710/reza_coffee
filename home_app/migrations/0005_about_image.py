# Generated by Django 4.0.3 on 2022-11-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(null=True, upload_to='AboutImage', verbose_name='عکس'),
        ),
    ]
