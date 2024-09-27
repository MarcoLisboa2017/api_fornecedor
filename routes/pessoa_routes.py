from flask import Blueprint, request, jsonify
from models import db, Pessoa
from schemas.pessoas_schemas import PessoaSchema
from marshmallow import ValidationError

pessoa_bp = Blueprint('pessoa_bp', __name__)

pessoa_schema = PessoaSchema()
pessoas_schema = PessoaSchema(many=True)

# Rota POST para criar cliente ou fornecedor
@pessoa_bp.route('/fornecedorcliente', methods=['POST'])
def create_pessoa():
    data = request.json
    tipo_pessoa_id = data.get('tipo_pessoa_id')  # Supondo que você está recebendo o ID do tipo

    try:
        pessoa_data = pessoa_schema.load(data)
        tipo_id = pessoa_data.pop('tipo_id') 
        
        # Remover 'tipo_pessoa_id' de pessoa_data, se existir
        pessoa_data.pop('tipo_pessoa_id', None)

        # Criar nova pessoa
        nova_pessoa = Pessoa(tipo_id=tipo_id, **pessoa_data, tipo_pessoa_id=tipo_pessoa_id)
        db.session.add(nova_pessoa)
        db.session.commit()
        
        return jsonify(pessoa_schema.dump(nova_pessoa)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota GET para listar ou buscar uma pessoa por ID
@pessoa_bp.route('/fornecedorcliente', methods=['GET'])
def get_pessoas():
    pessoa_id = request.args.get('id')

    if pessoa_id:
        # Buscar pessoa específica por ID
        pessoa = Pessoa.query.get(pessoa_id)
        if not pessoa:
            return jsonify({"message": "Pessoa não encontrada"}), 404
        return jsonify(pessoa_schema.dump(pessoa)), 200
    else:
        # Listar todas as pessoas
        pessoas = Pessoa.query.all()
        return jsonify(pessoas_schema.dump(pessoas)), 200
