# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: managementController.py
# Ultima modificação: 01/02/2018
from _model.myModel import *
from _model.myPlot import *
import json

# classe Management
# 	- Backoffice da aplicação
class Management():

	def __init__(self):
		pass

	# Função que executa ações de acordo a ação:
	# @param action -> ação
	def db_action(action):
		if(action == 'load'):
			Management.__drop_all()
			Management.__load_all()
			return "Dados carregados com sucesso!"
		elif(action == 'drop'):
			Management.__drop_all()
			return "Dados apagados com sucesso!"
		elif(action == 'graph'):
			Management.__etcsUc()
			Management.__publicationYear()
			Management.__teachersCourseType()
			return "Gráficos gerados com sucesso!"
		else:
			return "Ocorreu um erro de ação..."

	# Função que apaga todos os dados da base de dados
	def __drop_all():
		try:
			db.session.query(Uc).delete()
			db.session.query(Academic).delete()
			db.session.query(Affiliation).delete()
			db.session.query(Publication).delete()
			db.session.query(UcTeacher).delete()
			db.session.query(Teacher).delete()
			db.session.query(Laboratory).delete()
			db.session.commit()
		except Exception as e:
			return "Erro on drop: "+e
		
	# Função que carrega todos os dados para a base de dados
	def __load_all():
		try:
			course_id="3"
			data = json.load(open('_scraping/'+course_id+'_ucs.txt'))
			for uc in data['uc']:
				new_uc = Uc(uc['name'], uc['etcs'], uc['semester'], uc['year'], uc['goals'], uc['program'], uc['evaluation_process'], uc['language'],uc['uc_style'],uc['uc_optional'])
				db.session.add(new_uc)
			db.session.commit()
			data = json.load(open('_scraping/'+course_id+'_teachers.json'))
			for teacher in data['teacher']:
				new_teacher = Teacher(teacher['id_teacher'], teacher['name'], teacher['photo_url'], teacher['phone'], teacher['resume'])
				db.session.add(new_teacher)
			db.session.commit()
			for academic in data['academic']:
				new_academic = Academic(academic['university'], CourseType.get_id(academic['type']), academic['course'],academic['ac_year'],academic['id_teacher'])
				db.session.add(new_academic)
			db.session.commit()
			for aff in data['affiliation']:
				new_affiliation = Affiliation(aff['affiliation_type'], aff['affiliation_unit'], aff['affiliation_unit_url'],aff['id_teacher'])
				db.session.add(new_affiliation)
			db.session.commit()
			for pub in data['publications']:
				new_publication = Publication(pub['pub_title'],pub['pub_local'],pub['pub_year'],pub['pub_type'],pub['pub_authors'],pub['id_teacher'])
				db.session.add(new_publication)
			db.session.commit()
			for uc in data['uc']:
				new_uc = UcTeacher(uc['name'],uc['url'],uc['id_teacher'])
				db.session.add(new_uc)
			db.session.commit()
			data = json.load(open('_scraping/'+course_id+'_laboratories.json'))
			for laboratory in data['laboratories']:
				new_lab = Laboratory(laboratory['title'], laboratory['info'], laboratory['list'])
				db.session.add(new_lab)
			db.session.commit()
		except Exception as e:
			return "Erro on load: "+e
		
	# Função que cria os gráficos etcs/ucs
	def __etcsUc():
		Y = []
		X = []
		for x in range(2,7):
			y = Uc.get_ucs_credits(x)
			Y.append(y)
			X.append(x)
		MyPlot.bar_graph(X, Y, 'etcs_uc', 'Nº de Ucs por ETCs', 'Nº ETCs', 'Nº UCs', X)
		MyPlot.linear_graph(X, Y, 'etcs_uc', 'Nº de UCs por ETCs', 'Nº ETCs', 'Nº UCs', X)

	# Função que cria os gráficos publicações/ano
	def __publicationYear():
		Y = []
		X = []
		for x in range(1988,2019):
			y = Publication.get_publication_year(x)
			Y.append(y)
			X.append(x)
		MyPlot.bar_graph(X, Y, 'publications_year', 'Nº de Publicações por Ano', 'Anos', 'Nº Publicações', X ,'vertical')
		MyPlot.linear_graph(X, Y, 'publications_year', 'Nº de Publicações por Ano', 'Anos', 'Nº Publicações', X ,'vertical')

	# Função que cria os gráficos docente/tipo de curso
	def __teachersCourseType():
		Y = []
		X = []
		XLabels = []
		ct = CourseType.get_course_type()
		for c in ct:
			y = Academic.get_academic_course(c.id_course_type)
			Y.append(y)
			X.append(c.id_course_type)
			XLabels.append(c.name)
		MyPlot.bar_graph(X, Y, 'teacher_ct', 'Nº de Professores por Graduação', 'Graduação', 'Nº Professores', XLabels)
		MyPlot.linear_graph(X,Y, 'teacher_ct', 'Nº de Professores por Graduação', 'Graduação', 'Nº Professores', XLabels)