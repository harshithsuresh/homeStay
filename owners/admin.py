from django.contrib import admin
from .models import Owner

class OwnerAdmin(admin.ModelAdmin):
    list_display=('id','name','email','phone','location')
    list_display_links=('id','name')
    search_fields=('name',)
    list_per_page=25

admin.site.register(Owner,OwnerAdmin)
