from flask import Blueprint, render_template
from ..models import Noticia

main_routes = Blueprint("main", __name__)

@main_routes.route("/home")
@main_routes.route("/")
def home():
    #get from api TODO
    
    return render_template("home.html")

@main_routes.route("/trilhas")
def trilhas():
    
    return render_template("trilhas.html")