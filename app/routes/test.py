from ..extensions import db
from flask import Blueprint
from ..models import Noticia

test_bp = Blueprint("tests", __name__)

titles = [
    "Curso de programação do Cesar School gratuito",
    "Bolsa 100% para universidades de tecnologia",
    "Bolsas FACEPE"
]

bodies = [
    "O Cesar School está oferecendo um curso gratuito de introdução à programação para jovens interessados em tecnologia. A iniciativa visa capacitar e incentivar novos talentos para o mercado de TI.",
    "Diversas universidades de tecnologia estão oferecendo bolsas integrais para cursos de graduação e pós-graduação. A oportunidade é voltada para estudantes com bom desempenho acadêmico e interesse na área tecnológica.",
    "A Fundação de Amparo à Ciência e Tecnologia do Estado de Pernambuco (FACEPE) está com inscrições abertas para bolsas de pesquisa em diversas áreas do conhecimento. O objetivo é fomentar a produção científica e a inovação no estado."
]

links = [
    "https://www.cesar.school/",
    "https://www.portal.capes.gov.br/bolsas/bolsas-no-pais",
    "https://www.facepe.br/"
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