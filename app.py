# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: app.py
# Ultima modificação: 01/02/2018
from flask import Flask
from flask import render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from templates._components.loginform import *
from templates._components.ucform import *
from _model.myModel import *
from _controller.managementController import *
from _filters.myFilters import *
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'iscte'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///_db/iscte.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'true'
db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'login'

Filters(app)

# Página de apresentação
@app.route('/')
@app.route('/index')
def index():
	if (current_user.is_authenticated):
		return render_template('index.html', user=current_user)
	else:
		return render_template('index.html')

# Página de planos de estudo que contém todas as informações das ucs
@app.route('/plano-estudos', methods=['GET', 'POST'])
def plano_estudos():
	ucs = Uc.get_ucs_plan()
	form = UcForm()
	if form.validate_on_submit():
		_filter = form.mysearch.data
		if (current_user.is_authenticated):
			return render_template('plano-estudos.html', user=current_user, ucs = ucs, form=form, _filter=_filter)
		else:
			return render_template('plano-estudos.html', ucs = ucs, form=form, _filter=_filter)
	if (current_user.is_authenticated):
		return render_template('plano-estudos.html', user=current_user, ucs = ucs, form=form, _filter='')
	else:
		return render_template('plano-estudos.html', ucs = ucs, form=form, _filter='')

# Página da empregabilidade que contém algumas testemunhas e estatisticas sobre o curso
@app.route('/empregabilidade')
def empregabilidade():
	if (current_user.is_authenticated):
		return render_template('empregabilidade.html', user=current_user)
	else:
		return render_template('empregabilidade.html')

# Página da lista de docentes
@app.route('/docentes')
def docentes():
	teachers = Teacher.get_teachers()
	if (current_user.is_authenticated):
		return render_template('docentes.html', teachers=teachers, user=current_user)
	else:
		return render_template('docentes.html', teachers=teachers)

# Página de informação de todos os detalhes do docente
@app.route('/docente/<_id>')
def docente(_id=None):
	if(_id == None):
		return redirect(url_for('docentes'))
	else:
		teacher = Teacher.get_teacher(_id)
		if(teacher):
			academic = Academic.get_academic(_id)
			ucs = UcTeacher.get_uc_teacher(_id)
			publications = Publication.get_publication_teacher(_id)
			if (current_user.is_authenticated):
				return render_template('docente.html', teacher=teacher, academics=academic, publications=publications, ucs=ucs, user=current_user)
			else:
				return render_template('docente.html', teacher=teacher, academics=academic, publications=publications, ucs=ucs)
			
		else:
			return redirect(url_for('docentes'))

# Página de informação dos laboratórios
@app.route('/laboratorios')
def laboratorios():
	labs = Laboratory.get_laboratories()
	if (current_user.is_authenticated):
		return render_template('laboratorios.html', labs=labs, user=current_user)
	else:
		return render_template('laboratorios.html', labs=labs)

# Página de estatisticas a partir da base de dados
@app.route('/estatisticas')
def estatisticas():
	n_ucs = Uc.get_ucs_count()
	n_pub = Publication.get_publications_count()
	n_teacher = Teacher.get_teachers_count()
	if (current_user.is_authenticated):
		return render_template('estatisticas.html', user=current_user, n_ucs=n_ucs, n_pub=n_pub, n_teacher=n_teacher)
	else:
		return render_template('estatisticas.html', n_ucs=n_ucs, n_pub=n_pub, n_teacher=n_teacher)

# Página de inicio de sessão
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.getUser_byEmail(form.email.data)
		if user:
			if user.password == form.password.data:
				user = User.load_user(user._id)
				login_user(user)
				return redirect(url_for('manutencao', user=user))
			else:
				return render_template('login.html', form=form, error="O email ou password incorretos.")      
		return render_template('login.html', form=form, error="O utilizador com o email "+form.email.data+" não existe.")
	return render_template('login.html', form=form, error="")

# Executa logout
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

# Página de erro 404 (segurança)
@app.errorhandler(404)
@app.route('/404')
def page_not_found(e):
	return render_template('404.html')

# Página de manuntenção/backoffice
@app.route('/manutencao', methods=['GET', 'POST'])
@login_required
def manutencao():
	error = ""
	if request.method == 'POST':
		action = request.form['submit'] 
		error = Management.db_action(action)
		return render_template('manutencao.html', user=current_user, error=error)
	elif request.method == 'GET':
		return render_template('manutencao.html', user=current_user, error=error)
