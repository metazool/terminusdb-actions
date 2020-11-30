import pytest
from terminusdb_client import WOQLClient

HOST = 'http://localhost:6363'

@pytest.fixture
def client():
    client = WOQLClient(HOST)
#    client.organization("admin")
    client.basic_auth("admin", "root")
    client.connect(key="root", account="admin", user="admin")
    return client

def test_create(client):
    client.create_database('test', accountid="admin")
