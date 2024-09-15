from app import app
from models import db, Moulin

with app.app_context():
    # Récupérer tous les moulins existants
    moulins = Moulin.query.all()

    # Ajouter une taille par défaut pour chaque moulin existant
    for moulin in moulins:
        if moulin.taille is None:  # Pour éviter de remplacer une taille existante
            moulin.taille = 15.0  # Par exemple, vous pouvez définir une taille par défaut de 15 cm

    db.session.commit()

print("Tous les moulins existants ont été mis à jour avec une taille par défaut.")
