from django.db import models


class Gazeteci(models.Model):
    isim = models.CharField(max_length=120)
    soyisim = models.CharField(max_length=120)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.isim} {self.soyisim}'


class Makale(models.Model):
    yazar = models.ForeignKey(Gazeteci, on_delete=models.CASCADE, related_name="makaleler")
    baslik = models.CharField(max_length=75)
    aciklama = models.CharField(max_length=150)
    metin = models.TextField(max_length=200)
    sehir = models.CharField(max_length=20)
    yayimlanma_tarihi = models.DateField()
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik
