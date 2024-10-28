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




