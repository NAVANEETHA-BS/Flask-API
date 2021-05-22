from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return '<Customer %r>' % self.name