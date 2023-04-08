# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import date

class Movie(db.Model):
    
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(180))
    poster = db.Column(db.String(100))
    created_at = db.Column(db.Date)
    
    def __init__(self, title, desc, poster):
        self.title = title
        self.desc = desc
        self.poster = poster
        
        today = date.today()
        created_at = today.strftime("%d/%m/%Y")
        
        self.created_at = created_at