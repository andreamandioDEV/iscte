# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: language.py
# Ultima modificação: 01/02/2018
from _model.shared import db

# classe Language:
#	- ligações com a tabela language da base de dados
class Language(db.Model):
	__tablename__ = "language"
	id_language = db.Column('id_language', db.Integer, primary_key=True, unique=True, autoincrement=True)
	name = db.Column('name', db.String(150))

	def __init__(self, name):
		self.name = name

	# Função para obter o nome do registo
	# com o id = x
	# @param _id -> id da linguagem
	# Refs: https://q-a-assistant.info/computer-internet-technology/querying-with-function-on-flask-sqlalchemy-model-gives-basequery-object-is-not-callable-error/3917139
	def get_name(_id):
		name = db.session.query(Language.name).filter_by(id_language=_id).scalar()
		return name