# Third-party imports...
from nose.tools import assert_true
import requests
from flask import jsonify


def test_registration():
    response = requests.post(
        url = "http://localhost/register",
        data = {
            "username": "jose",
            "password": "asdf"
        }
    )

    assert (
        (
                (response.text.strip() == '{"message": "A user with username \'jose\' already exists."}') &
                (response.status_code == 400)
        ) |
        (
                (response.text.strip() == '{"message": "User created successfully."}') &
                (response.status_code == 201)
        )
    )

def test_login():
    response = requests.post(
        url = "http://localhost/login",
        data = {
            "username": "jose",
            "password": "asdf"
        }
    )

    print(response.text)
    # response_dict = dict(response.text)
    # access_token = response_dict['access_token']
    # print(access_token)

    assert False
