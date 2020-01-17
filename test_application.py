import requests
import json


def test_registration():
    response = requests.post(
        url = "http://localhost/register",
        json = {
            "username": "jose",
            "password": "asdf"
        }
    )

    response_dict = json.loads(response.text)

    assert (
        (
                (response_dict["message"] == "A user with username 'jose' already exists.") &
                (response.status_code == 400)
        ) |
        (
                (response_dict["message"] == "User created successfully.") &
                (response.status_code == 201)
        )
    )

def test_login():
    response = requests.post(
        url = "http://localhost/login",
        json = {
            "username": "jose",
            "password": "asdf"
        }
    )

    response_dict = json.loads(response.text)
    access_token = response_dict['access_token']

    assert (not (access_token == "")) & (response.status_code == 200)

def test_delete_piano_if_it_exists():
    response = requests.delete(
        url = "http://localhost/item/piano"
    )

    response_dict = json.loads(response.text)

    assert response_dict["message"] == "Item deleted"
    assert response.status_code == 200

def test_delete_pianostore_if_it_exists():
    response = requests.delete(
        url = "http://localhost/store/pianostore"
    )

    response_dict = json.loads(response.text)

    assert response_dict["message"] == "Store deleted."
    assert response.status_code == 200

def test_make_pianostore():
    response = requests.post(
        url = "http://localhost/store/pianostore"
    )

    response_dict = json.loads(response.text)

    if response.status_code == 400:
        assert response_dict["message"] == "A store with name pianostore already exists."
    elif response.status_code == 201:
        assert (
            (response_dict["name"] == "pianostore") &
            (response_dict["items"] == [])
        )
    else:
        assert False

def test_get_stores_with_no_items():
    response = requests.get(
        url = "http://localhost/stores"
    )

    response_dict = json.loads(response.text)

    assert response_dict["stores"][0]["name"] == "pianostore"
    assert response_dict["stores"][0]["items"] == []
    assert response.status_code == 200

def test_create_piano_at_pianostore():
    response = requests.post(
        url = "http://localhost/item/piano",
        json = {
            "price": 15.99,
            "store_name": "pianostore"
        }
    )

    response_dict = json.loads(response.text)

    if response.status_code == 201:
        assert (
            (response_dict["name"] == "piano") &
            (response_dict["price"] == 15.99)
        )
    elif response.status_code == 400:
        assert response_dict["message"] == "An item with name 'piano' already exists."
    else:
        assert False

def test_get_stores_with_items():
    response = requests.get(
        url = "http://localhost/stores"
    )

    response_dict = json.loads(response.text)

    assert response_dict["stores"][0]["name"] == "pianostore"
    assert response_dict["stores"][0]["items"][0]["name"] == "piano"
    assert response_dict["stores"][0]["items"][0]["price"] == 15.99
    assert response.status_code == 200

def test_update_piano_price():
    response = requests.put(
        url = "http://localhost/item/piano",
        json = {
            "price": 17.99,
            "store_name": "pianostore"
        }
    )

    response_dict = json.loads(response.text)

    assert response_dict["name"] == "piano"
    assert response_dict["price"] == 17.99
    assert response.status_code == 200

def test_get_stores_with_updated_items():
    response = requests.get(
        url = "http://localhost/stores"
    )

    response_dict = json.loads(response.text)

    assert response_dict["stores"][0]["name"] == "pianostore"
    assert response_dict["stores"][0]["items"][0]["name"] == "piano"
    assert response_dict["stores"][0]["items"][0]["price"] == 17.99
    assert response.status_code == 200

def test_jwt_and_get_piano():
    response = requests.post(
        url = "http://localhost/login",
        json = {
            "username": "jose",
            "password": "asdf"
        }
    )

    response_dict = json.loads(response.text)
    access_token = response_dict['access_token']

    response = requests.get(
        url = "http://localhost/item/piano",
        headers = {
            "Authorization": "JWT " + access_token
        }
    )

    response_dict = json.loads(response.text)

    assert response_dict["name"] == "piano"
    assert response_dict["price"] == 17.99
    assert response.status_code == 200

def test_get_items():
    response = requests.get(
        url = "http://localhost/items"
    )

    response_dict = json.loads(response.text)

    assert response_dict["items"][0]["name"] == "piano"
    assert response_dict["items"][0]["price"] == 17.99
    assert response.status_code == 200
