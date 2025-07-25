from flask import Blueprint, render_template
from ..models import Noticia
from ..utils import populate_db

main_routes = Blueprint("main", __name__)

@main_routes.route("/home")
@main_routes.route("/")
def home():
    ns = Noticia.query.all()
    
    if not len(ns):
        populate_db()
    
    noticias = []
    for n in ns:
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

# parcialmente implementado
# apenas suporta a trilha frontend
@main_routes.route("/trilhas/<nome>")
def trilha_rota(nome):
    return render_template("trilha_frontend.html")
    