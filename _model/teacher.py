# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: teacher.py
# Ultima modificação: 01/02/2018
from _model.shared import db

# classe Teacher:
#   - ligações com a tabela teacher da base de dados
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

	# Função para obter todos os registos 
	def get_teachers():
		return Teacher.query.all()

	# Função para obter o registo do
	# docente com o id = x
	# @param id_teacher -> id do docente
	def get_teacher(id_teacher):
		teacher = db.session.query(Teacher).filter_by(id_teacher=id_teacher).scalar()
		return teacher

	# Função para obter a contagem de todos os registos 
	def get_teachers_count():
		return Teacher.query.count()