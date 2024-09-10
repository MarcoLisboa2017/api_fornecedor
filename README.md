# api_fornecedor

# Inicando projeto
*python3 -m venv venv

*source venv/bin/activate

*pip install flask flask-mysql flask-sqlalchemy pymysql marshmallow

# Iniciar aplicação
source venv/bin/activate

Dentro da pasta do seu projeto, rode o comando para iniciar o servidor Flask:

*export FLASK_APP=app.py

*export FLASK_ENV=development
flask run

# Desativar o ambiente virtual
deactivate

# Como testar
url: http://localhost:5000/fornecedorcliente - POST

Body Json:
{
    "tipo": "cliente",
    "tipo_pessoa": "Física",
    "categoria": "Consumidor",
    "nome": "João Silva",
    "data_nascimento": "1985-10-23",
    "genero": "masculino",
    "cpf": "123.456.789-00",
    "celular": "(11) 98765-4321",
    "email": "joao@exemplo.com",
    "cep": "01000-000",
    "endereco": "Rua Exemplo",
    "numero": "123",
    "bairro": "Centro",
    "cidade": "São Paulo",
    "estado": "SP",
    "pais": "Brasil"
}

# Ajustar configuração de DB

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://USERNAME:SENHA@NOME BANCO DE DADOS /cliente_fornecedor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False