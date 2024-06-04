import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_get_resultados_nba(client):
    response = client.get('/v1/resultados_nba')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 3
    assert data[0]["time_casa"] == "Los Angeles Lakers"
