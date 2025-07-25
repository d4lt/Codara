from app.extensions import db
class Noticia(db.Model):
    __tablename__ = "noticias"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text)
    link = db.Column(db.Text, nullable=False)
    
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'), nullable=True)
    # todo: Date


#PRIORITY: mostrar a empresa com maior prioridade primeiro
class Empresa(db.Model):
    __tablename__ = "empresas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Integer, nullable=False)