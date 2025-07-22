from flask import Blueprint, render_template
from ..models import Noticia

main_routes = Blueprint("main", __name__)

@main_routes.route("/")
def home():
    
    
    return render_template("base.html")