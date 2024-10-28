from chalice import Chalice

app = Chalice(app_name='products')




users = {
            "users" : [
                {"products": "A", "amounts": "4"},
                {"products": "B", "amounts": "3"},
                {"products": "B", "amounts": "1"}

            ]    
}


@app.route('/products', methods = ["POST"])
def CreateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Produto {requestsParams} criado com sucesso"
    }
    return response



@app.route('/products', methods = ["PUT"])
def UpdateUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Produto {requestsParams} atualizado com sucesso"
    }
    return response



@app.route('/products', methods = ["DELETE"])
def DeleteUser():
    requestsParams = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Produto {requestsParams} deletado com sucesso"
    }
    return response


@app.route('/products', methods = ["GET"])
def GetUser():
    response = {
        "statusCode": 200,
        "body": users
    }
    return response

@app.route('/products/{id}', methods = ["GET"])
def GetUser(id):
    response = {
        "statusCode": 200,
        "body": {id :{"products": "A", "amounts": "4"}}
    }
    return response

