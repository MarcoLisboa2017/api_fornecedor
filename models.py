from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Tipo(db.Model):
    __tablename__ = 'tipos'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50), unique=True, nullable=False)

    # Relação com a tabela Pessoa
    pessoas = db.relationship('Pessoa', backref='tipo', lazy=True)

class TipoPessoa(db.Model):
    __tablename__ = 'tipos_pessoa'
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50), unique=True, nullable=False)

    # Relação com a tabela Pessoa
    pessoas = db.relationship('Pessoa', backref='tipo_pessoa', lazy=True)
   

class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    id = db.Column(db.Integer, primary_key=True)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipos.id'), nullable=False)
    tipo_pessoa_id = db.Column(db.Integer, db.ForeignKey('tipos_pessoa.id'), nullable=False)  # Chave estrangeira
    categoria = db.Column(db.String(100))
    nome = db.Column(db.String(150), nullable=False)
    data_nascimento = db.Column(db.Date)
    genero = db.Column(db.String(50))
    cpf = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    telefone = db.Column(db.String(20))
    ramal = db.Column(db.String(10))
    email = db.Column(db.String(100))
    site_perfil = db.Column(db.String(200))
    observacao = db.Column(db.Text)
    cep = db.Column(db.String(20))
    endereco = db.Column(db.String(150))
    numero = db.Column(db.String(20))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    pais = db.Column(db.String(50))
    complemento = db.Column(db.String(100))
    referencia = db.Column(db.String(150))
    rg = db.Column(db.String(20))
    orgao_expedidor = db.Column(db.String(50))
    data_emissao = db.Column(db.Date)
    passaporte = db.Column(db.String(50))
    nif = db.Column(db.String(50))
    estrangeiro = db.Column(db.Boolean, default=False)
    inscricao_produto_rural = db.Column(db.String(50))
    profissao = db.Column(db.String(100))
    empregador = db.Column(db.String(100))
    estado_civil = db.Column(db.String(50))  # Casado/Solteiro
    inicio_atividade = db.Column(db.Date)
    final_atividade = db.Column(db.Date)
    atividade_encerrada = db.Column(db.Boolean, default=False)

    # Contatos adicionais
    contatos_adicionais = db.relationship('Contato', backref='pessoa', lazy=True)

class Contato(db.Model):
    __tablename__ = 'contatos'
    id = db.Column(db.Integer, primary_key=True)
    tipo_contato = db.Column(db.String(50))
    relacao = db.Column(db.String(50))  # Representante legal
    nome_contato = db.Column(db.String(150), nullable=False)
    data_nascimento = db.Column(db.Date)
    genero = db.Column(db.String(50))  # Masculino/Feminino
    celular = db.Column(db.String(20))
    telefone = db.Column(db.String(20))
    ramal = db.Column(db.String(10))
    fax = db.Column(db.String(20))
    email = db.Column(db.String(100))
    site_perfil = db.Column(db.String(200))
    observacao = db.Column(db.Text)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'), nullable=False)


# Adicionando os modelos de Produto e Estoque
class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    codigo_produto = db.Column(db.String(50), nullable=False, unique=True)
    marca = db.Column(db.String(50), nullable=False)
    unidade = db.Column(db.String(10), nullable=False)
    codigo_gtin = db.Column(db.String(50))
    ncm = db.Column(db.String(20))
    valor_venda = db.Column(db.Float, nullable=False)
    valor_custo = db.Column(db.Float, nullable=False)
    peso_bruto = db.Column(db.Float, nullable=False)
    peso_liquido = db.Column(db.Float, nullable=False)
    tamanho_produto = db.Column(db.String(50))
    origem_produto = db.Column(db.String(50))
    numero_ordem = db.Column(db.String(50))
    tipo_classificacao = db.Column(db.String(50))
    situacao = db.Column(db.String(10), nullable=False)  # Ativo/Inativo
    tipo = db.Column(db.String(50))
    eh_kit = db.Column(db.Boolean, default=False)  # Produto é um kit?
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))  # Relacionamento com fornecedor
    codigo_barras_interno = db.Column(db.String(50))
    aliquota_icms = db.Column(db.Float)
    aliquota_ipi = db.Column(db.Float)
    aliquota_pis = db.Column(db.Float)
    aliquota_cofins = db.Column(db.Float)
    unidade_tributavel = db.Column(db.String(10))
    codigo_beneficio_fiscal = db.Column(db.String(50))
    codigo_cest = db.Column(db.String(50))
    tributarias_federal = db.Column(db.String(50))
    tributarias_estadual = db.Column(db.String(50))
    parametros_nfe = db.Column(db.Boolean, default=False)
    parametros_nfce = db.Column(db.Boolean, default=False)
    observacoes = db.Column(db.Text)

    # Relacionamento com estoque
    estoque = db.relationship('Estoque', back_populates='produto', uselist=False)

class Estoque(db.Model):
    __tablename__ = 'estoques'

    id = db.Column(db.Integer, primary_key=True)
    localizacao = db.Column(db.String(100), nullable=False)
    estoque_inicial = db.Column(db.Float, nullable=False)
    estoque_minimo = db.Column(db.Float, nullable=False)
    estoque_maximo = db.Column(db.Float, nullable=False)
    estoque_atual = db.Column(db.Float, nullable=False) 

    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    produto = db.relationship('Produto', back_populates='estoque')

