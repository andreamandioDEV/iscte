# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: publication.py
# Ultima modificação: 01/02/2018
from _model.shared import db

# classe Publication:
#   - ligações com a tabela publication da base de dados
class Publication(db.Model):
	__tablename__ = "publication"
	id_publication = db.Column('id_publication', db.Integer, primary_key=True, unique=True, autoincrement=True)
	title = db.Column('title', db.String)
	local = db.Column('local', db.String)
	year = db.Column('year', db.String)
	type = db.Column('type', db.String)
	authors = db.Column('authors', db.String)
	id_teacher = db.Column('id_teacher', db.Integer)

	def __init__(self, title, local, year, type, authors, id_teacher):
		self.title = title
		self.local = local
		self.year = year
		self.type = type
		self.authors = authors
		self.id_teacher = id_teacher

	# Função para obter todos os registos 
	def get_publications():
		return Publication.query.all()

	# Função para obter todos os registos do
	# docente com o id = x
	# @param id_teacher -> id do docente
	def get_publication_teacher(id_teacher):
		publication = db.session.query(Publication).filter_by(id_teacher=id_teacher)
		return publication

	# Função para obter todos os registos
	# no ano = x
	# @param year -> ano da publicação
	def get_publication_year(year):
		return Publication.query.filter_by(year=year).count()

	# Função para obter a contagem de todos os registos 
	def get_publications_count():
		return Publication.query.count()

	



