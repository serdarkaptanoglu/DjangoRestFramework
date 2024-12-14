import requests
from pprint import pprint


def client():
    token = 'Token cd74c53a3572d59dbcc35495f04ae04a23b69acb'

    headers = {
        'Authorization': token,
    }

    response = requests.get(
        url='http://127.0.0.1:6001/api/kullanici-profilleri/',
        headers=headers,
    )
    print('Status Code: ', response.status_code)
    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
