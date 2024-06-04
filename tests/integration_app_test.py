import os
import pytest
from dotenv import load_dotenv, find_dotenv
import pymongo
import mongomock
from bson.objectid import ObjectId
from todo_app import app


@pytest.fixture
def client():
    filepath = find_dotenv(".env.test")
    load_dotenv(filepath, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client


def test_index_page(client):
    get_mock_mongo_collection()
    response = client.get('/')

    html_response = response.data.decode()

    assert response.status_code == 200
    assert 'Test todo (From integration test)' in html_response


def get_mock_mongo_collection():
    todo = {
        '_id': ObjectId('61a7fab58503e36eb6295414'), 'status': 'To do', 'name': 'Test todo (From integration test)', 
        'description': 'test description'
    }
    mongo_client = pymongo.MongoClient(os.environ.get('PRIMARY_CONNECTION_STRING'))
    db = mongo_client[os.environ.get('MONGO_DB_NAME')]
    items_collection = db[os.environ.get('COLLECTION_NAME')]
    items_collection.insert_one(todo)

