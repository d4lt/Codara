from flask import Flask
from .routes.main import main_routes
from .routes.test import test_bp
from .extensions import db

def create_app():
    app = Flask(__name__, template_folder="./templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
    # app.config['DEBUG'] = True
    app.register_blueprint(main_routes)
    app.register_blueprint(test_bp)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    
    return app