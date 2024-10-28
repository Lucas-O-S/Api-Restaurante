from chalice.test import Client
from app import app
import json


def test_CreateProducts():
    with Client(app) as client:
        response = client.http.post('/products',
                                    body=json.dumps({"products": "A", "amounts": "4"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_UpdateProducts():
    with Client(app) as client:
        response = client.http.put('/products',
                                    body=json.dumps({"products": "A", "amounts": "4"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_DeleteProducts():
    with Client(app) as client:
        response = client.http.delete('/products',
                                    body=json.dumps({"products": "A", "amounts": "4"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetProducts():
    with Client(app) as client:
        response = client.http.get('/products')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetProductsId():
    with Client(app) as client:
        response = client.http.get('/products/1')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200
