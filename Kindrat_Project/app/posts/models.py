from datetime import datetime
import enum
from .. import db

class PostType(enum.Enum):
    SPORT = 1
    NEWS = 2
    MEMES = 3
    PUBLICATION = 4
    OTHER = 5

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String(1000))
    image = db.Column(db.String(255), default='postdefault.jpg')
    created = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    type = db.Column(db.Enum(PostType), default="PUBLICATION")
    enabled = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('{self.title}', '{self.created}')"
