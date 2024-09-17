from flask import Flask
from models import db
from config import Config
from flask_migrate import Migrate
from pessoa_routes import pessoa_bp  # Importa as rotas de pessoa (cliente e fornecedor)
from product_routes import product_bp  # Importa as rotas de produto
from orcamento_routes import orcamento_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

# Registrar o Blueprint das rotas de cliente e fornecedor
app.register_blueprint(pessoa_bp)

# Registrar o Blueprint para as rotas de produto e estoque
app.register_blueprint(product_bp)


app.register_blueprint(orcamento_bp)

if __name__ == "__main__":
    app.run(debug=True)
