from flask import current_app
from app import db


class Rental(db.Model):
    pass
    # rental_id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String)
    # description =db.Column(db.String)
    # completed_at = db.Column(db.DateTime, nullable=True
