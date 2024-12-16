from django.urls import path,include
from profiller.api.views import ProfilViewSet, ProfilDurumViewSet, ProfilFotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiller', ProfilViewSet),
router.register(r'durumlar', ProfilDurumViewSet, basename='durum'),

urlpatterns = [
    path('', include(router.urls)),
    path('profil_foto/', ProfilFotoUpdateView.as_view(), name='profil-foto'),
]
