# Generated by Django 4.0.3 on 2022-09-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_for_show', models.CharField(max_length=100)),
                ('important_title', models.CharField(max_length=100)),
                ('discription', models.TextField(null=True)),
                ('discount', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('views', models.IntegerField(null=True)),
                ('slug', models.SlugField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='posts', to='blog.category')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'ایجاد پست جدید',
                'ordering': ('-created',),
            },
        ),
    ]