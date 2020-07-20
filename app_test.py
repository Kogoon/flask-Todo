from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    # GET /
    # HTTP Status Code : 200
    # Hello World
    assert response.status_code == 200
    assert b'{"text":Hello World!!' in response.data


