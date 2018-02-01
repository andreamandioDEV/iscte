from _model.myModel import *
class Filters():
	def __init__(self, app):	
		'''
		Filters
		Refs: http://librosweb.es/libro/explore_flask/chapter_8/custom_filters.html
		'''
		@app.template_filter('get_language_name')
		def get_language_name(_id):
			return Language.get_name(_id)

		@app.template_filter('get_affiliation')
		def get_affiliation(id_teacher):
			return Affiliation.get_affiliation(id_teacher)

		@app.template_filter('get_academic')
		def get_academic(id_teacher):
			return Academic.get_academic(id_teacher)

		@app.template_filter('get_course_type_name')
		def get_course_type_name(id_course):
			return CourseType.get_course_type_name(id_course)

		@app.template_filter('get_uc_teacher')
		def get_uc_teacher(id_teacher):
			return UcTeacher.get_uc_teacher(id_teacher)

		@app.template_filter('get_publication_teacher')
		def get_publication_teacher(id_teacher):
			return Publication.get_publication_teacher(id_teacher)

		#---------------------------------------------------------