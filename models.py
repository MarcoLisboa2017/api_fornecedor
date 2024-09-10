from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # cliente/fornecedor
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


class TipoPessoa(db.Model):
    __tablename__ = 'tipos_pessoa'
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50), unique=True, nullable=False)

    # Relação com a tabela Pessoa
    pessoas = db.relationship('Pessoa', backref='tipo_pessoa', lazy=True)