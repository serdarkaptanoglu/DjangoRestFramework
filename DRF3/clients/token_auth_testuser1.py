import requests
from pprint import pprint


def client():
    credentials = {
        'username': 'test_user1',
        'password': 'username123'
    }

    response = requests.post(
        url='http://127.0.0.1:6001/dj-rest-auth/login/',
        data=credentials
    )

    print('status code:', response.status_code)
    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
    