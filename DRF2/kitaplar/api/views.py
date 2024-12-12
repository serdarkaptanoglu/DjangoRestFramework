from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from kitaplar.models import Kitap, Yorum
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from kitaplar.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
from django.core.exceptions import ValidationError
from kitaplar.api.pagination import LargePagination


class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all().order_by('id')
    serializer_class = KitapSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = LargePagination


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        kullanici = self.request.user
        yorumlar = Yorum.objects.filter(kitap=kitap, yorum_sahibi=kullanici)
        if yorumlar.exists():
            raise ValidationError('Bir kitaba sadece bir yorum yapabilirsiniz.')
        serializer.save(kitap=kitap, yorum_sahibi=kullanici)


class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsYorumSahibiOrReadOnly]


"""
class KitapListCreateAPIViews(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
"""