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





