import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_resultados_nba(client):
    rv = client.get('/v1/resultados_nba')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert len(json_data) == 3
    assert json_data[0]['time_casa'] == 'Los Angeles Lakers'
