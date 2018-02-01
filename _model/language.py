from _model.shared import db

class Language(db.Model):
    __tablename__ = "language"
    id_language = db.Column('id_language', db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column('name', db.String(150))

    def __init__(self, name):
    	self.name = name

    def get_name(_id):
        #Refs: https://q-a-assistant.info/computer-internet-technology/querying-with-function-on-flask-sqlalchemy-model-gives-basequery-object-is-not-callable-error/3917139
        name = db.session.query(Language.name).filter_by(id_language=_id).scalar()
        return name