from chalice.test import Client
from app import app
import json


def test_CreatePerson():
    with Client(app) as client:
        response = client.http.post('/consumers/person',
                                    body=json.dumps({"name":"usuario01","phone":"479999999"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_UpdatePerson():
    with Client(app) as client:
        response = client.http.put('/consumers/person',
                                    body=json.dumps({"name":"usuario01","phone":"479999999"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_DeletePerson():
    with Client(app) as client:
        response = client.http.delete('/consumers/person',
                                    body=json.dumps({"name":"usuario01","phone":"479999999"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetPerson():
    with Client(app) as client:
        response = client.http.get('/consumers/person')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetPersonId():
    with Client(app) as client:
        response = client.http.get('/consumers/person/1')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_CreateCompany():
    with Client(app) as client:
        response = client.http.post('/consumers/company',
                                    body=json.dumps({"name":"usuario01","phone":"479999999"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_UpdateCompany():
    with Client(app) as client:
        response = client.http.put('/consumers/company',
                                    body=json.dumps({"name":"usuario01","phone":"479999999"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_DeleteCompany():
    with Client(app) as client:
        response = client.http.delete('/consumers/company',
                                    body=json.dumps({"name":"usuario01","phone":"479999999"}),
                                    headers={"Content-Type": "application/json"}
                                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetCompany():
    with Client(app) as client:
        response = client.http.get('/consumers/company')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_GetCompanyId():
    with Client(app) as client:
        response = client.http.get('/consumers/company/1')
        print(response.json_body)
        assert response.json_body["statusCode"] == 200
