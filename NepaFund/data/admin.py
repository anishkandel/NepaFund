from django.contrib import admin
from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display=('id','name','email','hire_date','phone', 'description')
    list_display_links=('id','name')
    search_fields=('name')
    list_per_page=25
admin.site.register(Data)
# Register your models here.
