from ..extensions import db
from flask import Blueprint
from ..models import Noticia

test_bp = Blueprint("tests", __name__)

titles = [
    "Santander abre 5 mil vagas para formação de mulheres em TI",
    "Bolsa Futuro Digital abre 1,5 mil vagas em cursos gratuitos de tecnologia; saiba como se inscrever",
    "Prefeitura do Recife lança edital e abre inscrições para o segundo ciclo do Programa Embarque Digital",
    "Fundação Edson Queiroz abre 485 vagas em cursos gratuitos para população em vulnerabilidade social"
]

bodies = [
    "",
    "",
    "",
    ""
]

links = [
    "https://www.santander.com.br/",
    "https://www.portal.capes.gov.br/bolsas/bolsas-no-pais",
    "https://www2.recife.pe.gov.br/",
    "https://unifor.br/fundacao-edson-queiroz"
]

@test_bp.route("/test")
def add_noticias():
    Noticia.query.delete()
    db.session.commit()
    
    for i in range(3):
        n = Noticia(title=titles[i], body=bodies[i], link=links[i])
        db.session.add(n)
    db.session.commit()
    
    ts = [n.title for n in Noticia.query.all()]
    
    return f"{ts}"