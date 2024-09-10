from flask import Flask, request, jsonify
from models import db, Pessoa, Contato
from schemas import PessoaSchema
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

pessoa_schema = PessoaSchema()
pessoas_schema = PessoaSchema(many=True)

@app.route('/fornecedorcliente', methods=['POST'])
def create_pessoa():
    data = request.json
    pessoa_data = pessoa_schema.load(data)
    nova_pessoa = Pessoa(**pessoa_data)
    db.session.add(nova_pessoa)
    db.session.commit()
    ##return pessoa_schema.jsonify(nova_pessoa)
    return pessoa_schema.dump(nova_pessoa), 201

if __name__ == "__main__":
    app.run(debug=True)
