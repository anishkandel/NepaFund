from django.contrib import admin
from .models import Platform
from platforms.choices import status_choices

class PlatformAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published', 'price','invest_date')
    list_display_links=('id','title')
    list_filter=('data',)
    list_editable=('is_published',)
    search_fields=('title','description','city','category','state','zipcode','price')
    list_per_page=25
admin.site.register(Platform, PlatformAdmin)