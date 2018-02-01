# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: course_type.py
# Ultima modificação: 01/02/2018
from _model.shared import db

# classe CourseType:
#   - ligações com a tabela course_type da base de dados
class CourseType(db.Model):
	__tablename__ = "course_type"
	id_course_type = db.Column('id_course_type', db.Integer, primary_key=True, unique=True, autoincrement=True)
	name = db.Column('name', db.String(150))

	def __init__(self, name):
		self.name = name

	# Função para obter o id do registo
	# com o nome = x
	# @param _name -> nome do tipo de curso
	def get_id(_name):
		_id = db.session.query(CourseType.id_course_type).filter_by(name=_name).scalar()
		if (_id == '' or _id == None or _id=='--'):
			return 6
		return _id

	# Função para obter o nome do registo
	# com o id = x
	# @param _id -> id do tipo de curso
	def get_course_type_name(_id):
		course_type_name = db.session.query(CourseType.name).filter_by(id_course_type=_id).scalar()
		return course_type_name

	# Função para obter todos os registos 
	def get_course_type():
		return CourseType.query.all()