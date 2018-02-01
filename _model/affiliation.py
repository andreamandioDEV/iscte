# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: affiliation.py
# Ultima modificação: 01/02/2018
from _model.shared import db

# classe Affiliation:
#	- ligações com a tabela affiliation da base de dados
class Affiliation(db.Model):
	__tablename__ = "affiliation"
	id_affiliation = db.Column('id_affiliation', db.Integer, primary_key=True, unique=True, autoincrement=True)
	type = db.Column('type', db.String(300))
	unit = db.Column('unit', db.String(300))
	unit_url = db.Column('unit_url', db.String(300))
	id_teacher = db.Column('id_teacher', db.Integer)

	def __init__(self, type, unit, unit_url,id_teacher):
		self.type = type
		self.unit = unit
		self.unit_url = unit_url
		self.id_teacher = id_teacher

	# Função para obter todos os registos 
	def get_affiliations():
		return Affiliation.query.all()

	# Função para obter todos os registos do
	# docente com o id = x
	# @param id_teacher -> id do docente
	def get_affiliation(id_teacher):
		affiliation = db.session.query(Affiliation).filter_by(id_teacher=id_teacher)
		return affiliation
	




