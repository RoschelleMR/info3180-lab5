# Add any model classes for Flask-SQLAlchemy here
from . import db

class Movie(db.Model):
    
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(180))
    poster = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(80))
    
    def __init__(self, title, desc, poster, created_at):
        self.title = title
        self.desc = desc
        self.poster = poster
        self.created_at = created_at