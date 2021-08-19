from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display=('id','userName','stayTitle','rating','stayID')
    list_display_links=('id','userName','stayTitle')
    list_per_page=25

admin.site.register(Review,ReviewAdmin)
