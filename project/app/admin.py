from django.contrib import admin
from .models import NewsCategory, News
# Register your models here.

# admin.site.register(NewsCategory)
# admin.site.register(News)

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('main', 'category', 'daten')
    list_filter = ('main', 'daten')
    search_fields = ('main',)
