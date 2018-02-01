from _model.shared import db

class UcTeacher(db.Model):
	__tablename__ = "uc_teacher"
	id_uc_teacher = db.Column('id_uc_teacher', db.Integer, primary_key=True, unique=True, autoincrement=True)
	name = db.Column('name', db.String)
	url = db.Column('url', db.String)
	id_teacher = db.Column('id_teacher', db.Integer)


	def __init__(self, name, url,id_teacher):
		self.name = name
		self.url = url
		self.id_teacher = id_teacher

	def get_uc_teachers():
		return UcTeacher.query.all()

	def get_uc_teacher(id_teacher):
		ucs = db.session.query(UcTeacher).filter_by(id_teacher=id_teacher)
		return ucs
	



