from app import db

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=False)
