from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls.conf import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('stays/',include('stays.urls')),
    path('accounts/',include('accounts.urls')),
    path('enquires/',include('enquires.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
