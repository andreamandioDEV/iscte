from _model.shared import db, login_manager

class User(db.Model):
    __tablename__ = "users"
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(150), unique=True)
    email = db.Column('email', db.String(150), unique=True)
    password = db.Column('password', db.String(80))
    created_at = db.Column('created_at' , db.DateTime)

    def getUser_byEmail(_email):
        user = User.query.filter_by(email=_email).first()
        return user

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(int(_id))

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return self._id
 
    def __repr__(self):
        return '<User %r>' % (self.email)
