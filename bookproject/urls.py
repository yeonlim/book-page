from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import book.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book.views.home, name="home"),
    path('book/', include('book.urls')),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
