from flask import Flask
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do .env
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configurações do Flask
    app.config['DEBUG'] = os.getenv('DEBUG', True)  # Valor padrão: True
    app.config['SECRET_KEY'] = os.getenv('KEY', 'default-secret-key')

    # Importa e registra o Blueprint
    from application.src.routes.home import home_
    app.register_blueprint(home_)

    return app
