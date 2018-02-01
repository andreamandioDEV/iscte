from _model.shared import db

class Academic(db.Model):
	__tablename__ = "academic"
	id_academic = db.Column('id_academic', db.Integer, primary_key=True, unique=True, autoincrement=True)
	university = db.Column('university', db.String(300))
	id_course_type = db.Column('id_course_type', db.Integer)
	course = db.Column('course', db.String(300))
	year = db.Column('year', db.String)
	id_teacher = db.Column('id_teacher', db.Integer)


	def __init__(self, university, id_course_type, course, year,id_teacher):
		self.university = university
		self.id_course_type = id_course_type
		self.course = course
		self.year = year
		self.id_teacher = id_teacher

	def get_academics():
		return Academic.query.all()

	def get_academic(id_teacher):
		academic = db.session.query(Academic).filter_by(id_teacher=id_teacher)
		return academic

	def get_academic_course(id_course_type):
		return Academic.query.filter_by(id_course_type=id_course_type).count()



