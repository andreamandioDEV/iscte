from _model.shared import db

class Uc(db.Model):
    __tablename__ = "uc"
    id_uc = db.Column('id_uc', db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column('name', db.String(150))
    etcs = db.Column('etcs', db.Float)
    semester = db.Column('semester', db.Integer)
    year = db.Column('year', db.Integer)
    goals = db.Column('goals', db.String(550))
    program = db.Column('program', db.String(550))
    evaluation_process = db.Column('evaluation_process', db.String(550))
    id_language = db.Column('id_language', db.Integer)
    id_uc_style = db.Column('id_uc_style', db.Integer)
    uc_optional = db.Column('uc_optional', db.Integer, default=0)

    def __init__(self, name, etcs, semester, year, goals, program, evaluation_process, id_language, id_uc_style, uc_optional=0):
    	self.name = name
    	self.etcs = etcs
    	self.semester = semester
    	self.year = year
    	self.goals = goals
    	self.program = program
    	self.evaluation_process = evaluation_process
    	self.id_language = id_language
    	self.id_uc_style = id_uc_style
    	self.uc_optional = uc_optional

    def get_ucs():
        return Uc.query.all()

    def get_ucs_count():
        return Uc.query.count()

    def get_ucs_semester_year(year,semester, id_uc_style, uc_optional):
        return Uc.query.filter_by(semester=semester, year=year, id_uc_style=id_uc_style, uc_optional=uc_optional).all()

    def get_ucs_plan():
        ucs = []
        ucs.append(Uc.get_ucs_semester_year(1,1, 1, 0))
        ucs.append(Uc.get_ucs_semester_year(1,2, 1, 0))
        ucs.append(Uc.get_ucs_semester_year(2,1, 1, 0))
        ucs.append(Uc.get_ucs_semester_year(2,2, 1, 0))
        ucs.append(Uc.get_ucs_semester_year(3,1, 1, 0))
        ucs.append(Uc.get_ucs_semester_year(3,2, 1, 0))
        ucs.append(Uc.get_ucs_semester_year(1,2, 2, 0))
        ucs.append(Uc.get_ucs_semester_year(1,2, 2, 1))
        return ucs

    def get_ucs_credits(num):
        return Uc.query.filter_by(etcs=num).count()



