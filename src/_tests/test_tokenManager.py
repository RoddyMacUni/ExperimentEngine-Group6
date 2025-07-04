import requests_mock
from api.TokenManager import TokenManager
import time

tm: TokenManager = TokenManager("http://localhost:2000/fake")
m = requests_mock.Mocker()
m.post('http://localhost:2000/fake/auth/login', json='{"token": "sampleApiToken"}')

def test_will_use_saved_token():
    with requests_mock.Mocker() as m:
        m.post('http://localhost:2000/fake/auth/login', text='{"token": "abc"}')

        tm.getToken()

        tm.token = "123"

        assert tm.getToken() == "123"

def test_will_fetch_new_token_if_none():
    with requests_mock.Mocker() as m:
        m.post('http://localhost:2000/fake/auth/login', text='{"token": "abc"}')

        tm.token = None

        assert tm.getToken() == "abc"

def test_will_refresh_token():
    with requests_mock.Mocker() as m:
        tm: TokenManager = TokenManager("http://localhost:2000/fake", 1)
        m.post('http://localhost:2000/fake/auth/login', text='{"token": "abc"}')

        tm.token = None

        assert tm.getToken() == "abc"

        m.post('http://localhost:2000/fake/auth/login', text='{"token": "abcd"}')
        assert tm.getToken() == "abc"
        time.sleep(2)
        assert tm.getToken() == "abcd"
