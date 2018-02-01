# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: laboratory.py
# Ultima modificação: 01/02/2018
from _model.shared import db

# classe Laboratory:
#	- ligações com a tabela laboratory da base de dados
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
		
	# Função para obter todos os registos 
	def get_laboratories():
		return Laboratory.query.all()



