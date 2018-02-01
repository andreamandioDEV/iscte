from _model.shared import db

class Teacher(db.Model):
	__tablename__ = "teacher"
	id_teacher = db.Column('id_teacher', db.Integer, primary_key=True, unique=True, autoincrement=True)
	name = db.Column('name', db.String(300))
	photo_url = db.Column('photo_url', db.String(300))
	phone = db.Column('phone', db.String(100))
	resume = db.Column('resume', db.String(3000))

	def __init__(self, id_teacher, name, photo_url, phone,resume):
		self.id_teacher = id_teacher
		self.name = name
		self.photo_url = photo_url
		self.phone = phone
		self.resume = resume

	def get_teachers():
		return Teacher.query.all()

	def get_teacher(id_teacher):
		teacher = db.session.query(Teacher).filter_by(id_teacher=id_teacher).scalar()
		return teacher

	def get_teachers_count():
		return Teacher.query.count()