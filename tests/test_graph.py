import pytest
from rdflib import Graph
from terminusdb_client import WOQLClient
from terminusdb_client import WOQLQuery as WQ
from terminusdb_client.woqlclient.errors import APIError

HOST = 'http://localhost:6363'


@pytest.fixture
def client():
    client = WOQLClient(HOST)
    client.connect(key="root", account="admin", user="admin", db="test")
    return client


def test_create(client):
    try:
        client.create_database('test', accountid="admin")
    except APIError as err:
        print(err.msg)
    with pytest.raises(APIError):
        client.create_database('test', accountid="admin")


def test_insert_file(client):
    g = Graph()
    g.parse('./data/lexicon-named-rock-unit.nt', format='nt')
    ttl = str(g.serialize(format='ttl'))
#    print(ttl)
    client.insert_triples("instance", "main", ttl, "ttl insert")
    result = WQ().limit(4).triple("v:X", "v:P", "v:Y").execute(client)
    print(result)
