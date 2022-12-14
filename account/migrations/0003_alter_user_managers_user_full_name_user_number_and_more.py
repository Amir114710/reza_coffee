# Generated by Django 4.0.3 on 2022-08-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='Full_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='full name'),
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='username'),
        ),
    ]
