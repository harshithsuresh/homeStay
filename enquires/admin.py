from django.contrib import admin
from .models import Enquire

class EnquiresAdmin(admin.ModelAdmin):
    list_display=('id','userName','email','stayTitle','stayId','email','phone','userId')
    list_display_links=('id','userName')
    search_fields=('userName','email')
    list_per_page=25

admin.site.register(Enquire,EnquiresAdmin)