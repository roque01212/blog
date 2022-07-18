from django.contrib import admin

# Register your models here.
from .models import Entry, Tag, Category

admin.site.register(Entry)
admin.site.register(Tag)
admin.site.register(Category)
