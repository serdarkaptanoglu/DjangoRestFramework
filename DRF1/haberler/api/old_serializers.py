from rest_framework import serializers
from haberler.models import Makale


class MakaleSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayimlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncellenme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Makale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslık', instance.baslik)
        instance.aciklama = validated_data.get("aciklama", instance.aciklama)
        instance.metin = validated_data.get("metin", instance.metin)
        instance.sehir = validated_data.get("sehir", instance.sehir)
        instance.yayimlanma_tarihi = validated_data.get("yayimlanma_tarihi", instance.yayimlanma_tarihi)
        instance.aktif = validated_data.get("aktif", instance.aktif)
        instance.save()
        return instance

    def validate(self, data):
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError('Başlık ve açıklama alanları aynı olamaz.Lütfen farklı bir açıklama giriniz')
        return data

    def validate_baslik(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(f'Başlık alanı minimum 10 karakter olmalıdır.Siz {len(value)} karakter girdiniz. ')
        return value
