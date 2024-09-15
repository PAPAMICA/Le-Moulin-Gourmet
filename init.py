from app import app
from models import db, Poivre, Moulin

with app.app_context():
    db.create_all()

with app.app_context():
    # Ajouter des poivres
    poivre1 = Poivre(
        nom='Poivre Noir de Malabar',
        description='Un poivre noir intense et aromatique.',
        pays_origine='Inde',
        intensite=7,
        utilisations='viande rouge, volaille'
    )

    poivre2 = Poivre(
        nom='Poivre Blanc de Penja',
        description='Un poivre blanc doux et parfumé.',
        pays_origine='Cameroun',
        intensite=5,
        utilisations='poisson, légumes'
    )

    db.session.add_all([poivre1, poivre2])
    db.session.commit()

    # Ajouter des moulins
    moulin1 = Moulin(
        photo='static/images/moulin1.jpg',
        modele='Modèle A',
        marque='Marque X',
        couleur='Noir',
        origine="Anniversaire 2024",
        type_moulin="poivre",
        poivre_id=poivre1.id
    )

    moulin2 = Moulin(
        photo='static/images/moulin2.jpg',
        modele='Modèle B',
        marque='Marque Y',
        couleur='Blanc',
        origine="Anniversaire 2024",
        type_moulin="poivre",
        poivre_id=poivre2.id
    )

    db.session.add_all([moulin1, moulin2])
    db.session.commit()
