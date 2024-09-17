from flask import Blueprint, request, jsonify
from models import db, Orcamento, Produto, Pessoa
from orcamento_schemas import OrcamentoSchema
from datetime import date, timedelta
from sqlalchemy.exc import IntegrityError

orcamento_bp = Blueprint('orcamento_bp', __name__)

orcamento_schema = OrcamentoSchema()
orcamentos_schema = OrcamentoSchema(many=True)

@orcamento_bp.route('/orcamentos', methods=['POST'])
def criar_orcamento():
    data = request.json

    # Verifica se todos os campos obrigatórios estão presentes
    required_fields = ['pessoas_id', 'produtos_id', 'valor_unitario', 'valor_ipi', 'valor_icms', 'modalidade_frete']
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Campo '{field}' é obrigatório"}), 400

    try:
        # Busca o cliente e o produto para garantir que existem
        pessoa = Pessoa.query.get(data['pessoas_id'])
        produto = Produto.query.get(data['produtos_id'])

        if not pessoa:
            return jsonify({"message": "Pessoa não encontrada"}), 404
        if not produto:
            return jsonify({"message": "Produto não encontrado"}), 404

        # Verifica se o número do orçamento já existe
        if Orcamento.query.filter_by(numero_orcamento=data['numero_orcamento']).first():
            return jsonify({"message": "Número do orçamento já existe"}), 400

        # Cálculo dos valores
        quantidade = data.get('quantidade_produto', 1)  # Valor padrão de 1 se não fornecido
        valor_unitario = data['valor_unitario']
        valor_ipi = data['valor_ipi']
        valor_icms = data['valor_icms']
        valor_frete = data.get('valor_frete', 0)
        valor_desconto = data.get('valor_desconto', 0)

        valor_total = quantidade * valor_unitario + valor_ipi + valor_icms
        preco_bruto = valor_total + valor_frete
        preco_liquido = preco_bruto - valor_desconto

        # Define o status padrão como 'Orçamento aguardando aprovação'
        status = data.get('status', 'Orçamento aguardando aprovação')

        # Determina o prazo de entrega com base no status
        if status == 'Aprovado':
            prazo_entrega = data.get('prazo_entrega', date.today() + timedelta(days=7))
        else:
            prazo_entrega = date.today() + timedelta(days=7)  # Define um valor padrão

        validade = data.get('validade', date.today() + timedelta(days=10))

        novo_orcamento = Orcamento(
            pessoas_id=data['pessoas_id'],
            vendedor=data.get('vendedor'),
            numero_orcamento=data['numero_orcamento'],
            produtos_id=data['produtos_id'],
            quantidade=quantidade,
            valor_ipi=valor_ipi,
            valor_icms=valor_icms,
            valor_unitario=valor_unitario,
            valor_total=valor_total,
            valor_frete=valor_frete,
            valor_desconto=valor_desconto,
            preco_bruto=preco_bruto,
            preco_liquido=preco_liquido,
            modalidade_frete=data['modalidade_frete'],
            transportadora=data.get('transportadora'),
            data_orcamento=date.today(),
            prazo_entrega=prazo_entrega,
            validade=validade,
            observacoes=data.get('observacoes'),
            anexo=data.get('anexo'),
            status=status
        )

        db.session.add(novo_orcamento)
        db.session.commit()

        return jsonify(orcamento_schema.dump(novo_orcamento)), 201

    except IntegrityError as e:
        db.session.rollback()
        print(str(e))  # Loga o erro detalhado no console
        return jsonify({"message": "Erro ao criar o orçamento"}), 500

@orcamento_bp.route('/orcamentos/<int:id>/status', methods=['PUT'])
def atualizar_status_orcamento(id):
    data = request.json
    novo_status = data.get('status')

    if novo_status not in ['Orçamento aguardando aprovação', 'Aprovado', 'Recusado']:
        return jsonify({"error": "Status inválido"}), 400

    orcamento = Orcamento.query.get(id)
    if not orcamento:
        return jsonify({"error": "Orçamento não encontrado"}), 404

    # Atualiza o status e o prazo de entrega
    orcamento.status = novo_status
    if novo_status == 'Aprovado':
        orcamento.prazo_entrega = data.get('prazo_entrega', date.today() + timedelta(days=7))
    elif novo_status == 'Recusado':
        orcamento.prazo_entrega = None

    db.session.commit()

    return jsonify(orcamento_schema.dump(orcamento)), 200

@orcamento_bp.route('/orcamentos', methods=['GET'])
def listar_orcamentos():
    orcamentos = Orcamento.query.all()
    return orcamentos_schema.jsonify(orcamentos), 200
