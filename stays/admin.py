from django.contrib import admin

from .models import Stay

class StayAdmin(admin.ModelAdmin):
    list_display=('id','title','city','pricePerPerson','maxNoPerson','avgReview','countReview','bathrooms','zipcode')
    list_display_links=('id','title')
    search_fields=('title','city','state','zipcode')
    list_per_page=25
    
admin.site.register(Stay,StayAdmin)