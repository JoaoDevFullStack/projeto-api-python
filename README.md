# Projeto API com C# e Cliente Python

## Objetivo do Projeto
Este projeto consiste em uma API desenvolvida em C# que recebe e manipula dados de pessoas, e um cliente Python para consumir essa API.

## Tecnologias utilizadas
- **API (C#)**: ASP.NET Core Web API
- **Cliente**: Python (requests)
- **Banco de Dados**: SQL Server (via Entity Framework Core)

## Passos para executar a API (C#)
1. Clone o repositório.
2. Navegue até a pasta `api-csharp`.
3. Execute o comando `dotnet run` para rodar a API localmente.
4. Acesse `http://localhost:5000` para interagir com a API.

## Passos para executar o Cliente (Python)
1. Clone o repositório.
2. Navegue até a pasta `cliente-python`.
3. Instale as dependências com `pip install requests`.
4. Execute o script Python com `python cliente.py`.

## Exemplo de chamadas e respostas da API
- **GET /api/pessoa/{id}**: Retorna os dados de uma pessoa.
- **POST /api/pessoa/importar**: Envia um arquivo CSV para importar dados de pessoas.
