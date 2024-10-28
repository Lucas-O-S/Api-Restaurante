from chalice import Chalice

app = Chalice(app_name='sales')


#Dicionarios feitos para testar api com vendas e Venda offlines
#dentro delas há uma lista com dicionarios dentro para testar 


sales = {
            "sales" : [
                {"consumer": "venda01", "value": "23.2", "food": "macarrão"},
                {"consumer": "venda01", "value": "32.1", "food": "abacate"},
                {"consumer": "venda01", "value": "2.00", "food": "suco"},

            ]    
}


@app.route('/sales/online', methods = ["POST"])
def CreateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"venda {requestsParams} criado com sucesso"
    }
    return response



@app.route('/sales/online', methods = ["PUT"])
def UpdateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"venda online {requestsParams} atualizada com sucesso"
    }
    return response



@app.route('/sales/online', methods = ["DELETE"])
def DeleteUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"venda online {requestsParams} deletada com sucesso"
    }
    return response


@app.route('/sales/online', methods = ["GET"])
def GetUser():
    response = {
        "statusCode": 200,
        "body": sales
    }
    return response

@app.route('/sales/online/{id}', methods = ["GET"])
def GetUser(id):
    response = {
        "statusCode": 200,
        "body": {id :{"consumer": "venda01", "value": "23.2", "food": "macarrão"}}
    }
    return response


@app.route('/sales/offline', methods = ["POST"])
def CreateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda offline {requestsParams} criado com sucesso"
    }
    return response



@app.route('/sales/offline', methods = ["PUT"])
def UpdateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda offline {requestsParams} atualizada com sucesso"
    }
    return response



@app.route('/sales/offline', methods = ["DELETE"])
def DeleteUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda offline {requestsParams} deletada com sucesso"
    }
    return response


@app.route('/sales/offline', methods = ["GET"])
def GetUser():
    response = {
        "statusCode": 200,
        "body": sales
    }
    return response

@app.route('/sales/offline/{id}', methods = ["GET"])
def GetUser(id):
    response = {
        "statusCode": 200,
        "body": {id :{"consumer": "venda01", "value": "23.2", "food": "macarrão"}}
    }
    return response








