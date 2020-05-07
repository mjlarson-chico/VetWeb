from django.contrib import admin

from .models import Category, Resources, Guides

# Register your models here.
admin.site.register(Category)
admin.site.register(Resources)
admin.site.register(Guides)
