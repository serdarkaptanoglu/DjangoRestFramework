import requests
from pprint import pprint


def client():
    credentials = {
        'username': 'test_user3',
        'email': 'test_user3@test.co',
        'password1': 'testing321..',
        'password2': 'testing321..',
    }

    response = requests.post(
        url='http://127.0.0.1:6001/dj-rest-auth/registration/',
        data=credentials,
    )

    print('Status Code: ', response.status_code)
    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
