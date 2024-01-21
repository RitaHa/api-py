from json import dumps

import requests

from config import POSTS_URI, POST_DETAILS_URI


def test_get_all_posts():
    user_id = 1
    response = requests.get(POSTS_URI)
    response_json = response.json()
    assert response.status_code == requests.codes.ok
    user_ids = [post['userId'] for post in response_json]
    assert user_id in user_ids


def test_get_post_details():
    expected_data = {'userId': 1,
                     'id': 1,
                     'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
                     'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
    response = requests.get(POST_DETAILS_URI)
    response_json = response.json()
    assert response.status_code == requests.codes.ok
    for key, value in expected_data.items():
        assert response_json[key] == value


def test_post_new_post():
    data = {'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
            'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}
    payload = dumps(data)
    response = requests.post(POSTS_URI, data=payload, headers=headers)
    assert response.status_code == requests.codes.created
    post_id = response.json()['id']
    assert isinstance(post_id, int)


def test_put_post():
    response = requests.put(POST_DETAILS_URI)
    assert response.status_code == requests.codes.ok
    post_id = response.json()['id']
    assert isinstance(post_id, int)


def test_patch_post():
    expected_data = {'userId': 1,
                     'id': 1,
                     'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
                     'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
    response = requests.patch(POST_DETAILS_URI)
    response_json = response.json()
    assert response.status_code == requests.codes.ok
    for key, value in expected_data.items():
        assert response_json[key] == value


def test_delete_post():
    response = requests.delete(POST_DETAILS_URI)
    response_json = response.json()
    assert response.status_code == requests.codes.ok
    assert len(response_json) == 0



