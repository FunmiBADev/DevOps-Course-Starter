import os
import pytest
from dotenv import load_dotenv, find_dotenv
import requests
from todo_app import app


@pytest.fixture
def client():
    # Use test environment config here
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create new app instance
    test_app = app.create_app()

    # Create client using the new app instance
    with test_app.test_client() as client:
        yield client


class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
        self.status_code = 200

    def json(self):
        return self.fake_response_data


def get_mock_trello(url, params={}):
    # The expected URL should match the URL format used in your application
    expected_url = f'https://api.trello.com/1/boards/64f6582da14testb49e12999999/lists'

    if url == expected_url:
        return get_mock_trello_cards()

    raise Exception(f'Integration test did not expect URL "{url}"')


def get_mock_trello_cards():
    fake_response_data = [{
        'id': '123abc',
        'name': 'To do',
        'cards': [{'id': '456', 'name': 'Test card'}, {'id': '459', 'name': 'Mock data for tests'}]
    }]
    return StubResponse(fake_response_data)


def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', get_mock_trello)

    # Pass the expected URL and updated params here
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()
    assert 'Mock data for tests' in response.data.decode()
