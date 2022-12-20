from django.contrib import admin
from apps.news.models import News, Comment


# Register Rural360 Published news to the admin site
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_date', 'is_publish')
    ordering = ['-updated_date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'body',  'created_date')
    list_filter = ('created_date',)
    search_fields = ('body',)























