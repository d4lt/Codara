from ..extensions import db
from flask import Blueprint
from ..models import Noticia

test_bp = Blueprint("tests", __name__)

@test_bp.route("/test")
def add_noticias():
    ts = populate_db()
    
    return f"{ts}"