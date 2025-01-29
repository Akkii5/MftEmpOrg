from app.models.database import db

class Employee(db.Model):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(50))
    org_code = db.Column(db.Integer, db.ForeignKey('organisations.code'), nullable=False)

    organisation = db.relationship("Organisation", backref="employees")
