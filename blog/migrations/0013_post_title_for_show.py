# Generated by Django 4.0.3 on 2022-10-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_options_remove_post_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_for_show',
            field=models.CharField(max_length=100, null=True, verbose_name='نام کالا'),
        ),
    ]
