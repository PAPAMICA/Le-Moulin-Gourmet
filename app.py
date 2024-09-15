from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Poivre, Moulin
from forms import RechercheForm, MoulinForm, FiltreMoulinForm, PoivreForm
from config import Config
from werkzeug.utils import secure_filename
import os
from flask_migrate import Migrate
from sqlalchemy import or_
import unicodedata
import re

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

def normalize_string(s):
    s = s.lower()
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')
    s = re.sub(r'\s+', '', s)
    return s

@app.route('/')
def index():
    return redirect(url_for('afficher_moulins'))

@app.route('/moulins', methods=['GET', 'POST'])
def afficher_moulins():
    form = FiltreMoulinForm()
    moulins = Moulin.query

    if form.validate_on_submit():
        # Filtrer par type
        if form.type_moulin.data != 'tous':
            moulins = moulins.filter_by(type_moulin=form.type_moulin.data)
        # Trier
        if form.tri.data == 'alpha':
            moulins = moulins.order_by(Moulin.marque, Moulin.modele)
        else:
            moulins = moulins.order_by(Moulin.date_ajout.desc())
    else:
        moulins = moulins.order_by(Moulin.date_ajout.desc())

    moulins = moulins.all()
    return render_template('moulins.html', moulins=moulins, form=form)

@app.route('/moulins/ajouter', methods=['GET', 'POST'])
def ajouter_moulin():
    form = MoulinForm()
    poivre_form = PoivreForm()

    if form.validate_on_submit():
        fichier_photo = form.photo.data
        if fichier_photo and fichier_photo.filename != '':
            nom_fichier = secure_filename(fichier_photo.filename)
            chemin_fichier = os.path.join(app.config['UPLOAD_FOLDER'], nom_fichier)
            fichier_photo.save(chemin_fichier)
            chemin_photo = 'uploads/' + nom_fichier
        else:
            chemin_photo = None  # Vous pouvez définir une image par défaut si nécessaire

        # Récupérer ou créer le poivre en fonction du nom saisi
        poivre_nom = form.poivre_nom.data.strip()
        poivre = Poivre.query.filter_by(nom=poivre_nom).first()
        if not poivre:
            # Si le poivre n'existe pas, demander à l'utilisateur de l'ajouter via la modal
            return render_template('ajouter_moulin.html', form=form, poivre_form=poivre_form, show_poivre_modal=True)
        else:
            nouveau_moulin = Moulin(
                photo=chemin_photo,
                modele=form.modele.data,
                marque=form.marque.data,
                couleur=form.couleur.data,
                origine=form.origine.data,
                poivre_id=poivre.id,
                type_moulin=form.type_moulin.data
            )
            db.session.add(nouveau_moulin)
            db.session.commit()
            return redirect(url_for('afficher_moulins'))
    else:
        return render_template('ajouter_moulin.html', form=form, poivre_form=poivre_form)

@app.route('/moulins/editer/<int:id>', methods=['GET', 'POST'])
def editer_moulin(id):
    moulin = Moulin.query.get_or_404(id)
    form = MoulinForm(obj=moulin)
    poivre_form = PoivreForm()

    # Pré-remplir le champ poivre_nom avec le nom du poivre associé
    if request.method == 'GET':
        if moulin.poivre:
            form.poivre_nom.data = moulin.poivre.nom

    if form.validate_on_submit():
        # Vérifier si une nouvelle image a été téléchargée
        fichier_photo = form.photo.data
        if fichier_photo and not isinstance(fichier_photo, str) and fichier_photo.filename != '':
            # Une nouvelle image a été téléchargée
            nom_fichier = secure_filename(fichier_photo.filename)
            chemin_fichier = os.path.join(app.config['UPLOAD_FOLDER'], nom_fichier)
            fichier_photo.save(chemin_fichier)
            moulin.photo = 'uploads/' + nom_fichier
        # Mettre à jour les autres champs
        moulin.modele = form.modele.data
        moulin.marque = form.marque.data
        moulin.couleur = form.couleur.data
        moulin.origine = form.origine.data
        moulin.type_moulin = form.type_moulin.data

        # Récupérer ou créer le poivre en fonction du nom saisi
        poivre_nom = form.poivre_nom.data.strip()
        poivre = Poivre.query.filter_by(nom=poivre_nom).first()
        if not poivre:
            # Si le poivre n'existe pas, demander à l'utilisateur de l'ajouter via la modal
            return render_template('editer_moulin.html', form=form, poivre_form=poivre_form, moulin=moulin, show_poivre_modal=True)
        else:
            moulin.poivre_id = poivre.id

        db.session.commit()
        return redirect(url_for('afficher_moulins'))
    else:
        return render_template('editer_moulin.html', form=form, poivre_form=poivre_form, moulin=moulin)

@app.route('/poivres/autocomplete', methods=['GET'])
def poivres_autocomplete():
    term = request.args.get('term')
    poivres = Poivre.query.filter(Poivre.nom.ilike(f'%{term}%')).all()
    poivres_list = [{'label': poivre.nom, 'value': poivre.nom} for poivre in poivres]
    return jsonify(poivres_list)

@app.route('/poivres/ajouter_ajax', methods=['POST'])
def ajouter_poivre_ajax():
    form = PoivreForm()
    if form.validate_on_submit():
        # Vérifier si le poivre existe déjà
        existing_poivre = Poivre.query.filter_by(nom=form.nom.data).first()
        if existing_poivre:
            return jsonify({'error': 'Ce poivre existe déjà.'}), 400

        # Créer le nouveau poivre
        nouveau_poivre = Poivre(
            nom=form.nom.data,
            description=form.description.data,
            pays_origine=form.pays_origine.data,
            intensite=form.intensite.data,
            utilisations=form.utilisations.data
        )
        db.session.add(nouveau_poivre)
        db.session.commit()
        return jsonify({'success': True, 'nom': nouveau_poivre.nom})
    else:
        return jsonify({'error': 'Formulaire invalide.'}), 400

@app.route('/recherche', methods=['GET'])
def recherche_page():
    # Cette route affiche la page de recherche initiale
    # Extraire tous les aliments uniques depuis les poivres
    aliments_dict = {}
    poivres = Poivre.query.all()
    for poivre in poivres:
        if poivre.utilisations:
            for aliment in poivre.utilisations.split(','):
                aliment_nom = aliment.strip()
                aliment_key = normalize_string(aliment_nom)
                aliments_dict[aliment_key] = aliment_nom

    # Trier les aliments par ordre alphabétique
    aliments_items = sorted(aliments_dict.items(), key=lambda x: x[1])

    return render_template('recherche.html', aliments=aliments_items)

@app.route('/recherche_moulins', methods=['POST'])
def recherche_moulins():
    data = request.get_json()
    aliments_selectionnes = data.get('aliments', [])

    print(f"Aliments sélectionnés : {aliments_selectionnes}")  # Debug

    if not aliments_selectionnes:
        print("Aucun aliment sélectionné.")  # Debug
        return jsonify({'moulins': []})

    # Créer les filtres OR pour chaque aliment sélectionné
    filters = [Poivre.utilisations.ilike(f"%{aliment}%") for aliment in aliments_selectionnes]
    print(f"Filtres utilisés : {[str(f) for f in filters]}")  # Debug

    poivres_correspondants = Poivre.query.filter(or_(*filters)).all()
    print(f"Poivres trouvés : {[poivre.nom for poivre in poivres_correspondants]}")  # Debug

    # Trouver les moulins qui contiennent ces poivres
    moulins_correspondants = Moulin.query.filter(
        Moulin.poivre_id.in_([poivre.id for poivre in poivres_correspondants])
    ).all()
    print(f"Moulins trouvés : {[moulin.modele for moulin in moulins_correspondants]}")  # Debug

    moulins_list = []
    for moulin in moulins_correspondants:
        moulins_list.append({
            'id': moulin.id,
            'photo': url_for('static', filename=moulin.photo) if moulin.photo else url_for('static', filename='images/default.png'),
            'modele': moulin.modele,
            'marque': moulin.marque,
            'couleur': moulin.couleur,
            'origine': moulin.origine,
            'type_moulin': moulin.type_moulin.capitalize(),
            'poivre': {
                'nom': moulin.poivre.nom,
                'description': moulin.poivre.description,
                'pays_origine': moulin.poivre.pays_origine,
                'intensite': moulin.poivre.intensite,
                'utilisations': moulin.poivre.utilisations,
            }
        })

    print(f"Moulins à renvoyer : {moulins_list}")  # Debug
    return jsonify({'moulins': moulins_list})

if __name__ == '__main__':
    app.run(debug=True)
