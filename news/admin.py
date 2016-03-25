from django.contrib import admin
from news.models import News, Comment
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    can_delete = True

class NewsAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(News, NewsAdmin)