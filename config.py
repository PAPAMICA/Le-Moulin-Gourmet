import os

class Config:
    SECRET_KEY = 'votre_clé_secrète'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///poivres.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
