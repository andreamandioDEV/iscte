# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: user.py
# Ultima modificação: 01/02/2018
from _model.shared import db, login_manager

# classe User:
#   - ligações com a tabela users da base de dados
class User(db.Model):
	__tablename__ = "users"
	_id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(150), unique=True)
	email = db.Column('email', db.String(150), unique=True)
	password = db.Column('password', db.String(80))
	created_at = db.Column('created_at' , db.DateTime)

	# Função para obter utilizador por email
	def getUser_byEmail(_email):
		user = User.query.filter_by(email=_email).first()
		return user

	# Função para carregar utilizador
	@login_manager.user_loader
	def load_user(_id):
		return User.query.get(int(_id))

	# Função para ver se está autenticado
	def is_authenticated(self):
		return True
 
	# Função para ver se está ativo
	def is_active(self):
		return True
 
	# Função para ver se é anónimo
	def is_anonymous(self):
		return False
 
	 # Função para obter o id
	def get_id(self):
		return self._id
 
	def __repr__(self):
		return '<User %r>' % (self.email)
