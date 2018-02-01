from _model.shared import db

class Laboratory(db.Model):
	__tablename__ = "laboratory"
	id_laboratory = db.Column('id_laboratory', db.Integer, primary_key=True, unique=True, autoincrement=True)
	title = db.Column('title', db.String(300))
	info = db.Column('info', db.Integer)
	list = db.Column('list', db.String(300))

	def __init__(self, title, info, list):
		self.title = title
		self.info = info
		self.list = list

	def get_laboratories():
		return Laboratory.query.all()



