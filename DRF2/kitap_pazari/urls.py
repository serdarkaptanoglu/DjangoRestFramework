from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('kitaplar.api.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
