from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Poivre(db.Model):
    __tablename__ = 'poivres'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    pays_origine = db.Column(db.String(100), nullable=True)
    intensite = db.Column(db.Integer, nullable=True)
    utilisations = db.Column(db.String(500), nullable=True)

    moulins = db.relationship('Moulin', backref='poivre', lazy=True)

class Moulin(db.Model):
    __tablename__ = 'moulins'
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(200), nullable=True)
    modele = db.Column(db.String(100), nullable=False)
    marque = db.Column(db.String(100), nullable=False)
    taille = db.Column(db.String(50), nullable=True)
    couleur = db.Column(db.String(50), nullable=False)
    origine = db.Column(db.String(100), nullable=False)
    type_moulin = db.Column(db.String(10), nullable=False)
    date_ajout = db.Column(db.DateTime, default=datetime.utcnow)
    poivre_id = db.Column(db.Integer, db.ForeignKey('poivres.id'), nullable=True)
