from app.models.database import db

class Organisation(db.Model):
    __tablename__ = "organisations"

    code = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(20), nullable=False)
    details = db.Column(db.String(20))
