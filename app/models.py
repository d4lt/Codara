from app.extensions import db
class Noticia(db.Model):
    __tablename__ = "noticias"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text)
    link = db.Column(db.Text, nullable=False)
    # todo: Date