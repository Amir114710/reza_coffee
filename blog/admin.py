from django.utils.html import format_html
from django.contrib import admin
from .models import Category , Post , IPAddress , Like , Poster , Comments , Notification 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class PostAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('important_title','title_for_show','price','discount','views','discription','image_tag')
    list_filter = ('important_title','price','categories')
    fieldsets = (
        (None, {'fields': ('important_title','title_for_show')}),
        ('اطلاعات اصلی', {'fields': ('image','price','discount','discription')}),
        ('جزییات', {'fields': ('views',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('important_title',),
            'fields': ('important_title' ,'title_for_show'),
        }),
    )
    search_fields = ('important_title',)
    ordering = ('important_title',)
    filter_horizontal = ()

    def image_tag(self,obj):
        return format_html('<img src="{0}" style="width:10em; height:10em;" />'.format(obj.image.url))
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(IPAddress)
admin.site.register(Like)
admin.site.register(Poster)
admin.site.register(Comments)
admin.site.register(Notification)
# admin.site.register(NotificationAll)
# admin.site.register(ShopCategory)
# admin.site.register(Shop)