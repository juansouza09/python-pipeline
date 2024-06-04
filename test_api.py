import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_resultados_nba(client):
    response = client.get('/v1/resultados_nba')
    assert response.status_code == 200
    assert b'Los Angeles Lakers' in response.data
    assert b'Golden State Warriors' in response.data
    assert b'Brooklyn Nets' in response.data
    assert b'Milwaukee Bucks' in response.data
    assert b'Los Angeles Clippers' in response.data
    assert b'Phoenix Suns' in response.data
