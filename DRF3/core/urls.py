from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/', include('profiller.api.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
