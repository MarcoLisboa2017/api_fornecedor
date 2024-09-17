from models import Produto, Estoque
from marshmallow import Schema, fields

class EstoqueSchema(Schema):
    id = fields.Int(dump_only=True)
    localizacao = fields.Str(required=True)
    estoque_inicial = fields.Float(required=True)
    estoque_minimo = fields.Float(required=True)
    estoque_maximo = fields.Float(required=True)
    estoque_atual = fields.Float(required=True) 
    # Campo produto_id para identificar o produto associado
    produto_id = fields.Int(required=True)

class ProdutoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    codigo_produto = fields.Str(required=True)
    marca = fields.Str()
    unidade = fields.Str()
    codigo_gtin = fields.Str()
    ncm = fields.Str()
    valor_venda = fields.Float()
    valor_custo = fields.Float()
    peso_bruto = fields.Float()
    peso_liquido = fields.Float()
    tamanho_produto = fields.Str()
    origem_produto = fields.Str()
    numero_ordem = fields.Int()
    tipo_classificacao = fields.Str()
    situacao = fields.Str()
    tipo = fields.Str()
    eh_kit = fields.Bool()
    fornecedor_id = fields.Int(required=True)
    codigo_barras_interno = fields.Str()
    aliquota_icms = fields.Float()
    aliquota_ipi = fields.Float()
    aliquota_pis = fields.Float()
    aliquota_cofins = fields.Float()
    unidade_tributavel = fields.Str()
    codigo_beneficio_fiscal = fields.Str()
    codigo_cest = fields.Str()
    tributarias_federal = fields.Str()
    tributarias_estadual = fields.Str()
    parametros_nfe = fields.Bool()
    parametros_nfce = fields.Bool()
    observacoes = fields.Str()

    # Relacionamento com Estoque
    estoque = fields.Nested(EstoqueSchema, only=['estoque_atual'], many=False)
