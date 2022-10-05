from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from account.models import User
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی ها')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='ادرس ای پی')
   
    def __str__(self):
        return self.ip_address
    class Meta:
        verbose_name = 'ای پی'
        verbose_name_plural = "ادرس ای پی"

class Post(models.Model):
    categories = models.ManyToManyField(Category , related_name='posts' , verbose_name='دسته بندی ها')
    title_for_show = models.CharField(max_length=100, verbose_name='نام کالا')
    important_title = models.CharField(max_length=100)
    discription = models.TextField(null=True, verbose_name='توضیحات')
    discount = models.IntegerField(null=True, verbose_name='قیمت اصلی')
    price = models.IntegerField(null=True, verbose_name='قیمت تخفیف خورده')
    views = models.IntegerField(null=True, verbose_name='تعداد بازدید پست')
    image = models.ImageField(null=True, verbose_name='عکس کالا' , upload_to='product_image')
    slug = models.SlugField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    hits = models.ManyToManyField(IPAddress , blank=True , related_name='hits' , verbose_name='بازدید ها')

    def __str__(self):
        return f'{self.title_for_show}--{self.discription}'

    class Meta:
        ordering = ('-created',)
        verbose_name = 'پست'
        verbose_name_plural = "ایجاد پست جدید"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.important_title)
        super(Post , self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:detail' , kwargs={'slug':self.slug})
        
class Like(models.Model):
    users = models.ForeignKey(User, related_name='likes2' , on_delete=models.CASCADE , verbose_name = 'کاربر')
    posts = models.ForeignKey(Post, related_name='likes2' , on_delete=models.CASCADE , verbose_name = 'مقاله')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.users.phone} - {self.posts.important_title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering = ("-created",)

