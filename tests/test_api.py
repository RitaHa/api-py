import requests

from config import POSTS, POST_DETAILS


def test_get_all_posts():
    response = requests.get(POSTS)
    assert response.status_code == requests.codes.ok


def test_get_post_details():
    expected_data = {"userId": 1,
                     "id": 1,
                     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}
    response = requests.get(POST_DETAILS)
    response_json = response.json()
    assert response.status_code == requests.codes.ok
    for key, value in expected_data.items():
        assert response_json[key] == value


def test_post_new_post():
    response = requests.post(POST_DETAILS)
    assert response.status_code == requests.codes.ok
    post_id = response.json()['id']
    assert isinstance(post_id, int)


def test_put_post():
    response = requests.put(POST_DETAILS)
    assert response.status_code == requests.codes.ok
    post_id = response.json()['id']
    assert isinstance(post_id, int)


def test_patch_post():
    expected_data = {"userId": 1,
                     "id": 1,
                     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}
    response = requests.patch(POST_DETAILS)
    response_json = response.json()
    assert response.status_code == requests.codes.ok
    for key, value in expected_data.items():
        assert response_json[key] == value


def test_delete_post():
    response = requests.delete(POST_DETAILS)
    response_json = response.json()
    assert response.status_code == requests.codes.ok
    assert len(response_json) == 0



