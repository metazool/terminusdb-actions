import pytest
from terminusdb_client import WOQLClient

HOST = 'http://localhost:6363'

@pytest.fixture
def client():
    client = WOQLClient('http://localhost:6363')
    client.basic_auth("root", "admin")
    return client

def test_create(client):
    client.create_database('test')
