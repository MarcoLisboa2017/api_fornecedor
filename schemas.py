from marshmallow import Schema, fields

class ContatoSchema(Schema):
    id = fields.Int(dump_only=True)
    tipo_contato = fields.Str()
    relacao = fields.Str()
    nome_contato = fields.Str(required=True)
    data_nascimento = fields.Date()
    genero = fields.Str()
    celular = fields.Str()
    telefone = fields.Str()
    ramal = fields.Str()
    fax = fields.Str()
    email = fields.Str()
    site_perfil = fields.Str()
    observacao = fields.Str()

class PessoaSchema(Schema):
    id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True)
    tipo_pessoa = fields.Str(required=True)
    categoria = fields.Str()
    nome = fields.Str(required=True)
    data_nascimento = fields.Date()
    genero = fields.Str()
    cpf = fields.Str()
    celular = fields.Str()
    telefone = fields.Str()
    ramal = fields.Str()
    email = fields.Str()
    site_perfil = fields.Str()
    observacao = fields.Str()
    cep = fields.Str()
    endereco = fields.Str()
    numero = fields.Str()
    bairro = fields.Str()
    cidade = fields.Str()
    estado = fields.Str()
    pais = fields.Str()
    complemento = fields.Str()
    referencia = fields.Str()
    rg = fields.Str()
    orgao_expedidor = fields.Str()
    data_emissao = fields.Date()
    passaporte = fields.Str()
    nif = fields.Str()
    estrangeiro = fields.Bool()
    inscricao_produto_rural = fields.Str()
    profissao = fields.Str()
    empregador = fields.Str()
    estado_civil = fields.Str()
    inicio_atividade = fields.Date()
    final_atividade = fields.Date()
    atividade_encerrada = fields.Bool()
    contatos_adicionais = fields.List(fields.Nested(ContatoSchema))
