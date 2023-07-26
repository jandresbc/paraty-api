from .database import db
from datetime import datetime

class netflix(db.Model):
    __tablename__ = 'netflix'

    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.String)
    type = db.Column(db.String)
    title = db.Column(db.String)
    director = db.Column(db.String)
    cast = db.Column(db.String)
    country = db.Column(db.String)
    date_added = db.Column(db.Date)
    release_year = db.Column(db.String)
    rating = db.Column(db.String)
    duration = db.Column(db.String)
    listed_in = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.Date, default=datetime.now())
    updated_at = db.Column(db.Date, default=datetime.now())