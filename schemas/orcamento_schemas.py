from marshmallow import Schema, fields
from models import Produto, Estoque, Orcamento

class OrcamentoSchema(Schema):
    id = fields.Int(dump_only=True)
    pessoas_id = fields.Int(required=True)
    vendedor = fields.Str(required=True)
    numero_orcamento = fields.Int(dump_only=True)
    produtos_id = fields.Int(required=True)
    quantidade_produto = fields.Int(required=True)
    valor_ipi = fields.Float(required=True)
    valor_icms = fields.Float(required=True)
    valor_unitario = fields.Float(required=True)
    valor_total = fields.Float(dump_only=True)  # Calculado automaticamente
    valor_frete = fields.Float()
    valor_desconto = fields.Float()
    desconto_percentual = fields.Boolean(default=False)
    preco_bruto = fields.Float(dump_only=True)  # Calculado automaticamente
    preco_liquido = fields.Float(dump_only=True)  # Calculado automaticamente
    modalidade_frete = fields.Str(required=True)
    transportadora = fields.Str()
    data_orcamento = fields.DateTime(dump_only=True)
    prazo_entrega = fields.Str()
    validade = fields.Str()
    observacoes = fields.Str()
    anexo = fields.Str()
    status = fields.Str(required=True, validate=lambda s: s in ['Orçamento aguardando aprovação', 'Aprovado', 'Recusado'])

    class Meta:
        fields = (
            'id', 'pessoas.id', 'vendedor', 'numero_orcamento', 'produtos_id', 'quantidade', 'valor_ipi', 
            'valor_icms', 'valor_unitario', 'valor_total', 'valor_frete', 'valor_desconto', 'preco_bruto', 
            'preco_liquido', 'modalidade_frete', 'transportadora', 'data_orcamento', 'prazo_entrega', 
            'validade', 'observacoes', 'anexo', 'status'
        )
