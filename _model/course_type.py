from _model.shared import db

class CourseType(db.Model):
    __tablename__ = "course_type"
    id_course_type = db.Column('id_course_type', db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column('name', db.String(150))

    def __init__(self, name):
    	self.name = name

    def get_id(_name):
        _id = db.session.query(CourseType.id_course_type).filter_by(name=_name).scalar()
        if (_id == '' or _id == None or _id=='--'):
        	return 6
        return _id

    def get_course_type_name(_id):
        course_type_name = db.session.query(CourseType.name).filter_by(id_course_type=_id).scalar()
        return course_type_name

    def get_course_type():
        return CourseType.query.all()