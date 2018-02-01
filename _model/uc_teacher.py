# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: uc_teacher.py
# Ultima modificação: 01/02/2018
from _model.shared import db

# classe UcTeacher:
#   - ligações com a tabela uc_teacher da base de dados
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

	# Função para obter todos os registos 
	def get_uc_teachers():
		return UcTeacher.query.all()

	# Função para obter todos os registos do
	# docente com o id = x
	# @param id_teacher -> id do docente
	def get_uc_teacher(id_teacher):
		ucs = db.session.query(UcTeacher).filter_by(id_teacher=id_teacher)
		return ucs
	



