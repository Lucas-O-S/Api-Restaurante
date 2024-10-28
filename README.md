# RestauranteAPI

## Introdução

**RestauranteAPI** é uma aplicação de estudo desenvolvida em Python, utilizando AWS Lambda, com o objetivo de explorar a criação e o funcionamento de APIs serverless. Este projeto simula um sistema básico de gerenciamento de restaurante, abordando operações comuns, como cadastro e consulta de itens de menu, pedidos e gerenciamento de clientes. 

Esta API foi projetada para ser independente, sem conexão com um backend tradicional, tornando-se uma solução ideal para quem deseja aprender mais sobre arquitetura serverless e computação em nuvem.

## Regras de Negócio

A **RestauranteAPI** é organizada em três principais áreas de negócio:

1. **Cadastro de Clientes**: O cadastro de clientes é dividido em duas categorias:
   - **Pessoa Física** : link_api/consumers/person
   - **Pessoa Jurídica** : link_api/consumers/company

2. **Vendas**: O sistema gerencia vendas em dois canais:
   - **Vendas Online** : link_api/sales/online
   - **Vendas Offline** : link_api/sales/offline

3. **Produtos** : link_api/products

Cada área possui operações completas de CRUD (Create, Read, Update, Delete) para facilitar o gerenciamento.

## Bibliotecas Utilizadas

A **RestauranteAPI** faz uso de várias bibliotecas para facilitar o desenvolvimento e garantir um ambiente de trabalho eficiente. As principais bibliotecas incluem:

### 1. Chalice

**Chalice** é um framework Python que simplifica a criação de APIs serverless na AWS. Ele permite que você escreva código Python e crie rapidamente APIs RESTful, aproveitando os recursos do AWS Lambda.

**Instalação**:
```bash
pip install chalice
```

### virtualenv

**virtualenv** é uma ferramenta que permite criar ambientes virtuais isolados para projetos Python. Isso é especialmente útil para gerenciar dependências de diferentes projetos, garantindo que cada um utilize suas próprias versões de bibliotecas, sem conflitos entre elas.

#### Instalação

Para instalar o **virtualenv**, você pode usar o `pip`. Execute o seguinte comando em seu terminal:

```bash
pip install virtualenv
````

### Pytest

**pytest** é uma estrutura de testes para Python que permite a escrita de testes de forma simples e escalável. Ele suporta testes de unidade e integração, tornando-se uma ferramenta valiosa para garantir que seu código funcione conforme o esperado. O pytest também fornece uma rica variedade de recursos, como fixtures, parametrização de testes e relatórios detalhados.

#### Instalação

Para instalar o **pytest**, você pode usar o `pip`. Execute o seguinte comando em seu terminal:

```bash
pip install pytest
````
## Explicação do Código

A **RestauranteAPI** é estruturada utilizando uma arquitetura de **microserviços**, onde cada serviço é responsável por uma funcionalidade específica do sistema. Essa abordagem permite maior escalabilidade e manutenção do código, uma vez que cada microserviço pode ser desenvolvido, testado e implantado de forma independente.

Cada microserviço está isolado em seu próprio **ambiente virtual** utilizando o **virtualenv**, o que garante que as dependências de cada serviço não conflitem entre si. Essa prática facilita a gestão das bibliotecas e versões necessárias para o funcionamento de cada parte da API, promovendo um desenvolvimento mais organizado e eficiente.

A modularidade da aplicação permite que novos serviços sejam facilmente adicionados ou modificados sem impactar outros componentes do sistema, tornando a arquitetura mais flexível e adaptável a mudanças.

## Documentação do Código - Clientes

### Importações

```python
from chalice import Chalice
A biblioteca Chalice é importada para criar a aplicação serverless.
````
Inicialização da Aplicação
````python
Copiar código
app = Chalice(app_name='consumers')
````
A aplicação Chalice é inicializada com o nome consumers, que identifica a API.

Estruturas de Dados
Dicionários são usados para armazenar dados de teste de usuários e empresas:

````python
users = {
    "users": [
        {"name": "Usuario01", "phone": "479999999"},
        {"name": "Usuario02", "phone": "479999999"},
        {"name": "Usuario03", "phone": "479999999"}
    ]    
}

companies = {
    "companies": [
        {"name": "Usuario01", "phone": "479999999"},
        {"name": "Usuario02", "phone": "479999999"},
        {"name": "Usuario03", "phone": "479999999"}
    ]
}
Endpoints para Consumidores (Clientes)
````
Criar Usuário
````python
@app.route('/consumers/person', methods=["POST"])
def CreateUser():
    ...
````
Método: POST
Descrição: Cria um novo usuário com os dados fornecidos no corpo da requisição.

Resposta: Retorna uma mensagem de sucesso com o status code 200.
Atualizar Usuário
````python
Copiar código
@app.route('/consumers/person', methods=["PUT"])
def UpdateUser():
    ...
````
Método: PUT
Descrição: Atualiza os dados de um usuário existente com os dados fornecidos no corpo da requisição.

Resposta: Retorna uma mensagem de sucesso com o status code 200.
Deletar Usuário
````python
Copiar código
@app.route('/consumers/person', methods=["DELETE"])
def DeleteUser():
    ...
````

Método: DELETE
Descrição: Remove um usuário com base nos dados fornecidos no corpo da requisição.
Resposta: Retorna uma mensagem de sucesso com o status code 200.
Obter Todos os Usuários
````python
Copiar código
@app.route('/consumers/person', methods=["GET"])
def GetUser():
    ...
````

Método: GET
Descrição: Retorna a lista de todos os usuários.
Resposta: Retorna os dados dos usuários com o status code 200.

Obter Usuário por ID
````python
Copiar código
@app.route('/consumers/person/{id}', methods=["GET"])
def GetUser(id):
    ...
````

Método: GET
Descrição: Retorna os dados de um usuário específico baseado no ID fornecido na URL.
Resposta: Retorna os dados do usuário com o status code 200.

Endpoints para Empresas
Os endpoints para empresas seguem a mesma estrutura que os de usuários, permitindo a criação, atualização, exclusão e obtenção de dados de empresas.

Criar Empresa
````python
Copiar código
@app.route('/consumers/company', methods=["POST"])
def CreateUser():
    ...
````

Método: POST
Descrição: Cria uma nova empresa com os dados fornecidos no corpo da requisição.
Resposta: Retorna uma mensagem de sucesso com o status code 200.
Atualizar Empresa
````python
Copiar código
@app.route('/consumers/company', methods=["PUT"])
def UpdateUser():
    ...
````

Método: PUT
Descrição: Atualiza os dados de uma empresa existente com os dados fornecidos no corpo da requisição.
Resposta: Retorna uma mensagem de sucesso com o status code 200.
Deletar Empresa
````python
Copiar código
@app.route('/consumers/company', methods=["DELETE"])
def DeleteUser():
    ...
````

Método: DELETE
Descrição: Remove uma empresa com base nos dados fornecidos no corpo da requisição.
Resposta: Retorna uma mensagem de sucesso com o status code 200.
Obter Todas as Empresas
````python
Copiar código
@app.route('/consumers/company', methods=["GET"])
def GetUser():
    ...
````

Método: GET
Descrição: Retorna a lista de todas as empresas.
Resposta: Retorna os dados das empresas com o status code 200.
Obter Empresa por ID
````python
Copiar código
@app.route('/consumers/company/{id}', methods=["GET"])
def GetUser(id):
    ...
````
## Documentação do Código - Produtos

### Importações

```python
from chalice import Chalice
A biblioteca Chalice é importada para criar a aplicação serverless.
```
Inicialização da Aplicação
```python
app = Chalice(app_name='products')
```
A aplicação Chalice é inicializada com o nome products, que identifica a API.

Estruturas de Dados
Um dicionário é usado para armazenar dados de teste de produtos:

```python
Copiar código
users = {
    "users": [
        {"products": "A", "amounts": "4"},
        {"products": "B", "amounts": "3"},
        {"products": "C", "amounts": "1"}
    ]    
}
```
Endpoints para Produtos
Criar Produto
```python
Copiar código
@app.route('/products', methods=["POST"])
def CreateUser():
    ...
```
Método: POST
Descrição: Cria um novo produto com os dados fornecidos no corpo da requisição.
Resposta: Retorna uma mensagem de sucesso com o status code 200.
Atualizar Produto
```python
Copiar código
@app.route('/products', methods=["PUT"])
def UpdateUser():
    ...
```
Método: PUT
Descrição: Atualiza os dados de um produto existente com os dados fornecidos no corpo da requisição.
Resposta: Retorna uma mensagem de sucesso com o status code 200.
Deletar Produto
```python
Copiar código
@app.route('/products', methods=["DELETE"])
def DeleteUser():
    ...
```
Método: DELETE
Descrição: Remove um produto com base nos dados fornecidos no corpo da requisição.
Resposta: Retorna uma mensagem de sucesso com o status code 200.
Obter Todos os Produtos
```python
Copiar código
@app.route('/products', methods=["GET"])
def GetUser():
    ...
```
Método: GET
Descrição: Retorna a lista de todos os produtos.
Resposta: Retorna os dados dos produtos com o status code 200.
Obter Produto por ID
```python
Copiar código
@app.route('/products/{id}', methods=["GET"])
def GetUser(id):
    ...
```
Método: GET
Descrição: Retorna os dados de um produto específico baseado no ID fornecido na URL.
Resposta: Retorna os dados do produto com o status code 200.




