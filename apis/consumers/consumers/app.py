from chalice import Chalice

app = Chalice(app_name='consumers')


#Dicionarios feitos para testar api com usuarios e empresas
#dentro delas há uma lista com dicionarios dentro para testar 


users = {
            "users" : [
                {"name": "Usuario01", "phone": "479999999"},
                {"name": "Usuario02", "phone": "479999999"},
                {"name": "Usuario03", "phone": "479999999"}

            ]    
}

companies = {
                "companies" : [
                    {"name": "Usuario01", "phone": "479999999"},
                    {"name": "Usuario02", "phone": "479999999"},
                    {"name": "Usuario03", "phone": "479999999"}
                ]
}

@app.route('/consumers/person', methods = ["POST"])
def CreateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuario {requestsParams} criado com sucesso"
    }
    return response



@app.route('/consumers/person', methods = ["PUT"])
def UpdateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuario {requestsParams} atualizado com sucesso"
    }
    return response



@app.route('/consumers/person', methods = ["DELETE"])
def DeleteUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuario {requestsParams} deletado com sucesso"
    }
    return response


@app.route('/consumers/person', methods = ["GET"])
def GetUser():
    response = {
        "statusCode": 200,
        "body": users
    }
    return response

@app.route('/consumers/person/{id}', methods = ["GET"])
def GetUser(id):
    response = {
        "statusCode": 200,
        "body": {id :{"name": "Usuario01", "phone": "479999999"}}
    }
    return response


@app.route('/consumers/company', methods = ["POST"])
def CreateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requestsParams} criado com sucesso"
    }
    return response



@app.route('/consumers/company', methods = ["PUT"])
def UpdateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requestsParams} atualizado com sucesso"
    }
    return response



@app.route('/consumers/company', methods = ["DELETE"])
def DeleteUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requestsParams} deletado com sucesso"
    }
    return response


@app.route('/consumers/company', methods = ["GET"])
def GetUser():
    response = {
        "statusCode": 200,
        "body": companies
    }
    return response

@app.route('/consumers/company/{id}', methods = ["GET"])
def GetUser(id):
    response = {
        "statusCode": 200,
        "body": {id :{"name": "Usuario01", "phone": "479999999"}}
    }
    return response








