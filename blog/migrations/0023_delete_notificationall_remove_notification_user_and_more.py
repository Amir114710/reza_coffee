# Generated by Django 4.0.3 on 2023-01-11 12:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0022_notificationall_alter_notification_content_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NotificationAll',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ManyToManyField(related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='انتخاب کاربر'),
        ),
    ]