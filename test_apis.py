import pytest
import json
import requests


def test_01_verify_get_service():
    request_url = "https://jsonplaceholder.typicode.com/posts"
    result = requests.get(request_url)
    print("Request URL : [{}]".format(request_url))
    print("Response Body : [{}]".format(result.text))
    json_response = json.loads(result.text)
    # verify that status code is 200
    assert result.status_code == 200
    # verify that API returns at least 100 records
    assert len(json_response) >= 100
    # verify the schema
    assert json_response[0]['title'] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"


def test_02_verify_status_code_get_api():
    request_url = "https://jsonplaceholder.typicode.com/posts/1"
    result = requests.get(request_url)
    print("Request URL : [{}]".format(request_url))
    print("Response Body : [{}]".format(result.text))
    json_response = json.loads(result.text)
    # verify that status code is 200
    assert result.status_code == 200
    # verify that API returns only one record
    assert len(json_response) == 4
    # verify that id in response matches the input (1)
    assert json_response['id'] == 1

def test_03_verify_invalid_request():
    request_url = "https://jsonplaceholder.typicode.com/invalidposts"
    result = requests.get(request_url)
    # log the complete request and response details for troubleshooting
    print("Request details : {}".format(request_url))
    print("Response details : {}".format(result.text))
    # verify that status code is 404
    assert result.status_code == 404

def test_04_verify_post_service():
    request_url = "https://jsonplaceholder.typicode.com/posts"
    print("request_URL:[{}]".format(request_url))
    # send body as string
    message_body = {"title": "foo", "body": "bar", "userId": 1}
    print("message_body:[{}]".format(message_body))
    result = requests.post(request_url, data=message_body)
    print("Request URL : [{}]".format(request_url))
    print("Response Body : [{}]".format(result.text))
    # verify that status code is 201
    assert result.status_code == 201

def test_05_veriry_put_service():
    request_url = "https://jsonplaceholder.typicode.com/posts/1"
    print("request_URL:[{}]".format(request_url))
    # send body as JSON
    message_body = {"id": 1, "title": "abc", "body": "xyz", "userId": 1}
    print("message_body:[{}]".format(message_body))
    result = requests.put(request_url, data=message_body)
    print("Request URL : [{}]".format(request_url))
    print("Response Body : [{}]".format(result.text))
    # verify that status code is 200
    assert result.status_code == 200

def test_06_verify_delete_service():
    request_url = "https://jsonplaceholder.typicode.com/posts/1"
    result = requests.delete(request_url)
    json_response = json.loads(result.text)
    print("Request details : {}".format(request_url))
    print("Response details : {}".format(result.text))
    # verify that status code is 200
    assert result.status_code == 200
    
