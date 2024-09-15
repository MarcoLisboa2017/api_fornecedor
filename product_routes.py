from flask import Blueprint, request, jsonify
from models import db, Produto, Estoque
from product_schemas import ProdutoSchema, EstoqueSchema
from marshmallow import ValidationError

product_bp = Blueprint('product_bp', __name__)

produto_schema = ProdutoSchema()
produtos_schema = ProdutoSchema(many=True)
estoque_schema = EstoqueSchema()

# Rotas de Produto
@product_bp.route('/produtos', methods=['POST'])
def create_produto():
    data = request.json
    try:
        produto_data = produto_schema.load(data)
        novo_produto = Produto(**produto_data)
        db.session.add(novo_produto)
        db.session.commit()
        return jsonify(produto_schema.dump(novo_produto)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@product_bp.route('/produtos/<int:id>', methods=['GET'])
def get_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404
    return jsonify(produto_schema.dump(produto))

@product_bp.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify(produtos_schema.dump(produtos))

# Rotas de Estoque
@product_bp.route('/estoque', methods=['POST'])
def create_estoque():
    data = request.json
    try:
        estoque_data = estoque_schema.load(data)
        novo_estoque = Estoque(**estoque_data)
        db.session.add(novo_estoque)
        db.session.commit()
        return jsonify(estoque_schema.dump(novo_estoque)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
