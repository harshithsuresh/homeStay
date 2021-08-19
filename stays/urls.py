from django.urls import path
from . import views

urlpatterns=[
    path('',views.stays,name='stays'),
    path('<int:stay_id>',views.stay,name='stay'),
    path('search',views.search,name='search'),
    path('review',views.review,name='review')
]