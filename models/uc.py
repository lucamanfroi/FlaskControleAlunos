from ..extensions import db

class Uc(db.Model):
    __tablename__ = "ucs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    tipo = db.Column(db.String(50))
    inicio = db.Column(db.Date)
    fim = db.Column(db.Date)

    def __repr__(self):
        return f"<Uc(nome={self.nome}, tipo={self.tipo}, inicio={self.inicio}, fim={self.fim})>"