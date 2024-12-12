from rest_framework import serializers
from haberler.models import Makale, Gazeteci
from datetime import datetime, date
from django.utils.timesince import timesince


class MakaleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()

    class Meta:
        model = Makale
        fields = '__all__'
        read_only_fields = ['id', 'yaratilma_tarihi', 'guncellenme_tarihi']

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.yayimlanma_tarihi
        if object.aktif:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return "Aktif Değil!"

    def validate_yayimlanma_tarihi(self, tarihdegeri):
        today = date.today()
        if tarihdegeri > today:
            raise serializers.ValidationError('Yayımlanma yarihi ileri bir tarih olamaz ')
        return tarihdegeri

    def validate(self, data):
        if data["baslik"] == data["aciklama"]:
            raise serializers.ValidationError("Başlık ve açiklama alanları aynı olamaz")
        return data


class GazeteciSerializer(serializers.ModelSerializer):
    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay',
    )

    class Meta:
        model = Gazeteci
        fields = '__all__'
