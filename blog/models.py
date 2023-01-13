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
class objects_manager(models.Manager):
    def sellers(self):
        return self.filter(sellerinfo=True)
class Post(models.Model):
    categories = models.ManyToManyField(Category , related_name='posts' , verbose_name='دسته بندی ها')
    title_for_show = models.CharField(max_length=100, verbose_name='نام کالا', null=True)
    important_title = models.CharField(max_length=100,verbose_name='نام کالا به اینگلیسی' , null=True)
    discription = models.TextField(null=True, verbose_name='توضیحات')
    discount = models.IntegerField(null=True, verbose_name='قیمت تخفیف خورده')
    price = models.IntegerField(null=True, verbose_name='قیمت اصلی')
    views = models.IntegerField(null=True, verbose_name='تعداد بازدید پست')
    image = models.ImageField(null=True, verbose_name='عکس کالا' , upload_to='product_image')
    sellerinfo = models.BooleanField(default=False , verbose_name='قابل فروش')
    objects = objects_manager()
    slug = models.SlugField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True , null=True)
    hits = models.ManyToManyField(IPAddress , blank=True , related_name='hits' , verbose_name='بازدید ها')

    def __str__(self):
        return f'{self.important_title}--{self.discription}'

    class Meta:
        ordering = ('-created',)
        verbose_name = 'پست'
        verbose_name_plural = "ایجاد پست جدید"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.important_title)
        super(Post , self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:detail' , kwargs={'slug':self.slug})
    
    def admin_image(self):
        return '<img src="%s"/>' % self.image
    admin_image.allow_tags = True
    
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


class Poster(models.Model):
	title = models.CharField(max_length=255, verbose_name = 'مبحث')
	image = models.ImageField(upload_to='poster_home_page', verbose_name = 'عکس مربوطه')
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural ="پوستر ها"
		verbose_name = "پوستر"

class Comments(models.Model):
    user = models.ForeignKey(User , related_name="comment" , on_delete=models.CASCADE , verbose_name = 'کاربر')
    posts = models.ForeignKey(Post, related_name="comment" , on_delete=models.CASCADE, verbose_name = 'پست')

    parent = models.ForeignKey('self' , on_delete=models.CASCADE , related_name = 'replies' , null=True , blank=True, verbose_name = 'پست جواب داده شده')

    message = models.CharField(max_length=50 , null=True, blank=True, verbose_name = 'نظرات')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.phone}-{self.posts.important_title}'

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        ordering = ('-created',)

class Notification(models.Model):
    user = models.ManyToManyField(User , related_name='notifications' , verbose_name="انتخاب کاربر")
    content = models.TextField(verbose_name="متن اعلان")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'اعلان'
        verbose_name_plural = 'اعلان ها'
        ordering = ('-created',)
        
# class NotificationAll(models.Model):
#     content = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.content
        
#     class Meta:
#         verbose_name = 'اعلان'
#         verbose_name_plural = 'اعلان های همگانی'
#         ordering = ('-created',)
# _______________________________________________________________________________

# class ShopCategory(models.Model):
#     title = models.CharField(max_length=100, verbose_name='نام دسته بندی ها')
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ('-created',)
#         verbose_name = "دسته بندی"
#         verbose_name_plural = "   دسته بندی ها برای کالا های در دست فروش"

# class Shop(models.Model):
#     category = models.ManyToManyField(ShopCategory , related_name='shops' , verbose_name='دسته بندی ها')
#     title_for_shows = models.CharField(max_length=100, verbose_name='نام کالا', null=True)
#     important_titles = models.CharField(max_length=100,verbose_name='نام کالا به اینگلیسی' , null=True)
#     discriptions = models.TextField(null=True, verbose_name='توضیحات')
#     discounts = models.IntegerField(null=True, verbose_name='قیمت تخفیف خورده')
#     prices = models.IntegerField(null=True, verbose_name='قیمت اصلی')
#     images = models.ImageField(null=True, verbose_name='عکس کالا' , upload_to='shop_image')
#     slugs = models.SlugField(null=True,blank=True)
#     createds = models.DateTimeField(auto_now_add=True , null=True)

#     def __str__(self):
#         return f'{self.important_titles}--{self.discriptions}'

#     class Meta:
#         ordering = ('-createds',)
#         verbose_name = 'فروشگاه'
#         verbose_name_plural = "ایجاد پست برای فروش"

#     def save(self, *args, **kwargs):
#         self.slugs = slugify(self.important_titles)
#         super(Shop , self).save(*args, **kwargs)