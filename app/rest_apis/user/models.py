from . import db
class User(db.Model):
    __tablename__ = "user_info"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    cnic = db.Column(db.String(120), unique=False, nullable=False)
    date_of_birth = db.Column(db.String(120), unique=False, nullable=False)
    province = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return "<User Info %r>" % self.id