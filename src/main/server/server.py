from flask import Flask
from src.main.routes.tag_routes import tags_routes_bp

app = Flask(__name__)
## registra as rotas que estão no arquivo tag_routes.
app.register_blueprint(tags_routes_bp) 