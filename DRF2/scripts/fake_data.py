import os
import random
import django
import requests
from django.contrib.auth.models import User
from faker import Faker

from kitaplar.api.serializers import KitapSerializer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitap_pazari.settings')
django.setup()


def set_user():
    fake = Faker(['en_US'])
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'

    user_check = User.objects.filter(username=u_name)
    while user_check.exists():
        u_name = u_name + str(random.randrange(1, 99))
        user_check = User.objects.filter(username=u_name)

    user = User(
        username=u_name,
        first_name=f_name,
        last_name=l_name,
        email=email,
        is_staff=fake.boolean(chance_of_getting_true=50),
    )
    user.set_password('testing321..')
    user.save()
    print('Kullanıcı kaydedildi..', u_name)


def kitap_ekle(konu):
    fake = Faker(['en_US'])
    url = 'https://openlibrary.org/search.json'
    payload = {'q': konu}
    response = requests.get(url, params=payload)

    if response.status_code != 200:
        print('Hatalı istek yapıldı..', response.status_code)
        return

    jsn = response.json()
    kitaplar = jsn.get('docs')

    for kitap in kitaplar:
        kitap_adi = kitap.get('title')
        data = dict(
            isim=kitap_adi,
            yazar=kitap.get('author_name')[0],
            aciklama='-'.join(kitap.get('edition_key')),
            yayın_tarihi=fake.date_time_between(start_date='-10y', end_date='now', tzinfo=None),
        )
        serializer = KitapSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('Kitap Kaydedildi:', kitap_adi)
        else:
            continue
