from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=200 , verbose_name='نام')
    email = models.EmailField(max_length=500 , verbose_name='ایمیل')
    phone = models.IntegerField(null=True , verbose_name='شماره تلفن')
    message = models.TextField(null=True, verbose_name='پیام')

    def __str__(self):
        return f'{self.name} و {self.message}'

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"

class About(models.Model):
    title = models.CharField(max_length=555 , verbose_name='موضوع')
    little_discription = models.CharField(max_length=555 , verbose_name='توضیحات جزعی')
    discription = models.TextField(null=True, verbose_name='توضیحات')
    image = models.ImageField(null=True, verbose_name='عکس' , upload_to='AboutImage')
    created = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره"
        verbose_name_plural = "درباره"
