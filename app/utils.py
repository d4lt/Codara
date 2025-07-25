from .models import Noticia, Empresa
from .extensions import db

empresas = [ 
            {
    'nome': 'Santander',
    'prioridade': 5
},
{
    'nome': 'CAPES',
    'prioridade': 4
},

{
    'nome': 'Prefeitura do Recife',
    'prioridade': 3
},
{
    'nome': 'Fundacao Edson Queiroz',
    'prioridade': 2
},
            ]

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

def populate_db():
    Empresa.query.delete()
    Noticia.query.delete()
    db.session.commit()
    
    for i in range(4):
        e = Empresa(name=empresas[i]['nome'], priority=empresas[i]['prioridade'])
        db.session.add(e)
    db.session.commit()
    
    es = Empresa.query.all()
    for i in range(4):
        e_id = es[i].id
        n = Noticia(title=titles[i], body=bodies[i], link=links[i], empresa_id=e_id)
        db.session.add(n)
    db.session.commit()
    
    ts = [n.title for n in Noticia.query.all()]
    return ts