import requests_mock
from api.TokenManager import TokenManager

tm: TokenManager = TokenManager("http://localhost:2000/fake")
m = requests_mock.Mocker()
m.get('http://localhost:2000/fake/auth/login', json='{"token": "sampleApiToken"}')

def test_will_use_saved_token():
    with requests_mock.Mocker() as m:
        m.get('http://localhost:2000/fake/auth/login', json='{"token": "abc"}')

        tm.token = "123"

        assert tm.getToken() == "123"

def test_will_fetch_new_token_if_none():
    with requests_mock.Mocker() as m:
        m.get('http://localhost:2000/fake/auth/login', json='{"token": "abc"}')

        tm.token = None

        assert tm.getToken() == "abc"