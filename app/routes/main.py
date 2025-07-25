from flask import Blueprint, render_template
from ..models import Noticia

main_routes = Blueprint("main", __name__)

@main_routes.route("/home")
@main_routes.route("/")
def home():
    noticias = []
    for n in Noticia.query.all():
        noticia = {
            'title': n.title,
            'body': n.body,
            'link': n.link
        }
        noticias.append(noticia)
    
    
    return render_template("home.html", noticias=noticias)

@main_routes.route("/trilhas")
def trilhas():
    
    return render_template("trilhas.html")