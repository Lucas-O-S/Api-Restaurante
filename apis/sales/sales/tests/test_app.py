from chalice.test import Client
from app import app
import json


def test_CreateOnline():
    with Client(app) as client:
        response = client.http.post('/sales/online',
                                    body=json.dumps({"consumer": "venda01", "value": "23.2", "food": "macarrão"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_UpdateOnline():
    with Client(app) as client:
        response = client.http.put('/sales/online',
                                    body=json.dumps({"consumer": "venda01", "value": "23.2", "food": "macarrão"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_DeleteOnline():
    with Client(app) as client:
        response = client.http.delete('/sales/online',
                                    body=json.dumps({"consumer": "venda01", "value": "23.2", "food": "macarrão"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetOnline():
    with Client(app) as client:
        response = client.http.get('/sales/online')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetOnlineId():
    with Client(app) as client:
        response = client.http.get('/sales/online/1')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_CreateOffline():
    with Client(app) as client:
        response = client.http.post('/sales/offline',
                                    body=json.dumps({"consumer": "venda01", "value": "23.2", "food": "macarrão"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_UpdateOffline():
    with Client(app) as client:
        response = client.http.put('/sales/offline',
                                    body=json.dumps({"consumer": "venda01", "value": "23.2", "food": "macarrão"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_DeleteOffline():
    with Client(app) as client:
        response = client.http.delete('/sales/offline',
                                    body=json.dumps({"consumer": "venda01", "value": "23.2", "food": "macarrão"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetOffline():
    with Client(app) as client:
        response = client.http.get('/sales/offline')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetOfflineId():
    with Client(app) as client:
        response = client.http.get('/sales/offline/1')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200
