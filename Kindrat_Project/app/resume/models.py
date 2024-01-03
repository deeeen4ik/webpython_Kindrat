from app import db

class Resume(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Resume {self.id}>"
