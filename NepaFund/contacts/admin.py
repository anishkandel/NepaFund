from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'platform', 'email', 'contact_date')
    list_display_links=('id','email','platform')
    search_fields=('name','email','platform')
    list_per_page=25

admin.site.register(Contact, ContactAdmin)
