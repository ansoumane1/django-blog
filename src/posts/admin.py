from django.contrib import admin

# Register your models here.
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_on', 'last_updated')
    list_editable = ('published',)

