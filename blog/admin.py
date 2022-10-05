from django.contrib import admin
from .models import Category , Post , IPAddress , Like

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(IPAddress)
admin.site.register(Like)