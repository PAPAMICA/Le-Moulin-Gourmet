from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileField, FileAllowed


class RechercheForm(FlaskForm):
    aliments = SelectMultipleField('Sélectionnez des aliments', choices=[], coerce=str)
    submit = SubmitField('Rechercher')

class MoulinForm(FlaskForm):
    photo = FileField('Photo', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images seulement !')
    ])
    modele = StringField('Modèle', validators=[DataRequired()])
    marque = StringField('Marque', validators=[DataRequired()])
    taille = StringField('Taille', validators=[DataRequired()])
    couleur = StringField('Couleur', validators=[DataRequired()])
    origine = StringField('Origine', validators=[DataRequired()])
    type_moulin = SelectField('Type', choices=[('poivre', 'Poivre'), ('sel', 'Sel'), ('autre', 'Autre')], validators=[DataRequired()])
    poivre_nom = StringField('Epice', validators=[DataRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField('Valider')

class FiltreMoulinForm(FlaskForm):
    type_moulin = SelectField('Type', choices=[('tous', 'Tous'), ('poivre', 'Poivre'), ('sel', 'Sel'), ('autre', 'Autres')])
    tri = SelectField('Trier par', choices=[('date', 'Date d\'ajout'), ('alpha', 'Ordre alphabétique')])
    submit = SubmitField('Filtrer')

class PoivreForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    pays_origine = StringField('Pays d\'Origine', validators=[DataRequired()])
    intensite = IntegerField('Intensité', validators=[DataRequired(), NumberRange(min=1, max=10)])
    utilisations = TextAreaField('Utilisations', validators=[DataRequired()])
    submit = SubmitField('Ajouter')
