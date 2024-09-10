from flask import Flask, request, jsonify
from models import db, Pessoa, Contato
from schemas import PessoaSchema
from config import Config
from flask_migrate import Migrate
from marshmallow import ValidationError  # Importando ValidationError

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

pessoa_schema = PessoaSchema()
pessoas_schema = PessoaSchema(many=True)

@app.route('/fornecedorcliente', methods=['POST'])
def create_pessoa():
    data = request.json
    tipo_pessoa_id = data.get('tipo_pessoa_id')  # Supondo que você está recebendo o ID do tipo

    try:
        pessoa_data = pessoa_schema.load(data)
        pessoa_data['tipo'] = 'cliente'  # Ou ajuste conforme necessário
        
        # Remover 'tipo_pessoa_id' de pessoa_data, se existir
        pessoa_data.pop('tipo_pessoa_id', None)

        # Criar nova pessoa
        nova_pessoa = Pessoa(**pessoa_data, tipo_pessoa_id=tipo_pessoa_id)
        db.session.add(nova_pessoa)
        db.session.commit()
        
        # Usar jsonify do Flask para retornar a resposta
        return jsonify(pessoa_schema.dump(nova_pessoa)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
