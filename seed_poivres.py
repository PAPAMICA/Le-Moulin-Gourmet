from app import app
from models import db, Poivre, Moulin

with app.app_context():
    db.create_all()


with app.app_context():
    poivres = [
        Poivre(
            nom='Poivre Noir de Tellicherry',
            description='Un poivre noir indien aux grains larges, offrant des notes boisées et fruitées.',
            pays_origine='Inde',
            intensite=7,
            utilisations='viandes rouges, volailles, légumes, sauces'
        ),
        Poivre(
            nom='Poivre Blanc de Muntok',
            description='Un poivre blanc délicat et aromatique, provenant de l\'île de Bangka.',
            pays_origine='Indonésie',
            intensite=5,
            utilisations='poissons, crustacés, volailles, légumes blancs'
        ),
        Poivre(
            nom='Poivre Vert de Madagascar',
            description='Un poivre vert frais, légèrement piquant avec des notes herbacées.',
            pays_origine='Madagascar',
            intensite=4,
            utilisations='viandes blanches, fruits de mer, salades, fromages frais'
        ),
        Poivre(
            nom='Poivre de Sichuan',
            description='Un poivre aux notes citronnées avec une sensation engourdissante unique.',
            pays_origine='Chine',
            intensite=6,
            utilisations='cuisine asiatique, plats sautés, viandes, fruits de mer'
        ),
        Poivre(
            nom='Baies Roses',
            description='Des baies au goût sucré et légèrement poivré, souvent utilisées pour leur couleur.',
            pays_origine='Brésil',
            intensite=3,
            utilisations='poissons, foie gras, salades, desserts'
        ),
        Poivre(
            nom='Poivre Long',
            description='Un poivre au goût chaud et sucré avec des notes de cannelle et de muscade.',
            pays_origine='Inde',
            intensite=6,
            utilisations='plats mijotés, currys, desserts épicés'
        ),
        Poivre(
            nom='Poivre Cubèbe',
            description='Un poivre au goût camphré avec des notes d\'eucalyptus et de menthe.',
            pays_origine='Indonésie',
            intensite=5,
            utilisations='gibiers, viandes marinées, légumes racines, infusions'
        ),
        Poivre(
            nom='Poivre de Timut',
            description='Un poivre avec des notes d\'agrumes, proche du poivre de Sichuan.',
            pays_origine='Népal',
            intensite=5,
            utilisations='poissons, fruits de mer, desserts aux agrumes, chocolat'
        ),
        Poivre(
            nom='Poivre Voatsiperifery',
            description='Un poivre sauvage aux arômes boisés et floraux avec une touche d\'agrumes.',
            pays_origine='Madagascar',
            intensite=4,
            utilisations='viandes blanches, risottos, légumes grillés, desserts'
        ),
        Poivre(
            nom='Poivre de Kampot',
            description='Un poivre cambodgien réputé pour sa qualité, avec des notes épicées et mentholées.',
            pays_origine='Cambodge',
            intensite=6,
            utilisations='viandes, fruits de mer, soupes épicées, légumes sautés'
        ),
        Poivre(
            nom='Poivre Noir de Sarawak',
            description='Un poivre malaisien aux arômes fruités et légèrement fumés.',
            pays_origine='Malaisie',
            intensite=5,
            utilisations='viandes, champignons, légumes racines, fromages'
        ),
        Poivre(
            nom='Poivre Rouge de Kampot',
            description='Un poivre rouge rare avec des notes sucrées et fruitées.',
            pays_origine='Cambodge',
            intensite=6,
            utilisations='viandes, desserts aux fruits, chocolat noir'
        ),
        Poivre(
            nom='Poivre Noir de Malabar',
            description='Le berceau du poivre, offrant des grains noirs intenses et aromatiques.',
            pays_origine='Inde',
            intensite=7,
            utilisations='viandes, plats épicés, légumes grillés'
        ),
        Poivre(
            nom='Poivre Blanc de Penja',
            description='Un poivre blanc africain au goût doux et raffiné.',
            pays_origine='Cameroun',
            intensite=5,
            utilisations='poissons, volailles, sauces crémeuses, œufs'
        ),
        Poivre(
            nom='Poivre Andaliman',
            description='Un poivre rare avec des notes citronnées et florales.',
            pays_origine='Indonésie',
            intensite=5,
            utilisations='poissons, fruits de mer, plats végétariens, currys légers'
        ),
        Poivre(
            nom='Poivre des Cimes',
            description='Un poivre sauvage aux arômes de pamplemousse et de mandarine.',
            pays_origine='Chine',
            intensite=4,
            utilisations='poissons, fruits de mer, desserts aux agrumes, infusions'
        ),
        Poivre(
            nom='Poivre de Tasmanie',
            description='Un poivre australien au goût puissant et épicé avec des notes fruitées.',
            pays_origine='Australie',
            intensite=8,
            utilisations='gibiers, viandes rouges, chocolat noir, fromages forts'
        ),
        Poivre(
            nom='Poivre de Jamaïque',
            description='Aussi appelé piment de la Jamaïque, avec des saveurs de cannelle, muscade et clou de girofle.',
            pays_origine='Jamaïque',
            intensite=5,
            utilisations='marinades, ragoûts, pâtisseries épicées, boissons'
        ),
        Poivre(
            nom='Poivre Noir de Lampong',
            description='Un poivre indonésien aux arômes forts et piquants.',
            pays_origine='Indonésie',
            intensite=7,
            utilisations='viandes, plats épicés, currys, nouilles sautées'
        ),
        Poivre(
            nom='Poivre Rouge de Phu Quoc',
            description='Un poivre vietnamien au goût sucré et épicé.',
            pays_origine='Vietnam',
            intensite=6,
            utilisations='viandes, poissons grillés, fruits tropicaux, desserts'
        ),
        Poivre(
            nom='Poivre Ashanti',
            description='Un poivre africain au goût musqué avec des notes de noix de muscade.',
            pays_origine='Ghana',
            intensite=5,
            utilisations='ragoûts épicés, soupes, sauces relevées, légumineuses'
        ),
        Poivre(
            nom='Poivre de Maniguette',
            description='Connu sous le nom de "Graines de Paradis", avec des notes chaudes et poivrées.',
            pays_origine='Afrique de l\'Ouest',
            intensite=6,
            utilisations='viandes grillées, poissons, couscous, pains épicés, infusions'
        ),
        Poivre(
            nom='Poivre de Selim',
            description='Un poivre en forme de gousse, au goût musqué et légèrement amer.',
            pays_origine='Afrique de l\'Ouest',
            intensite=4,
            utilisations='soupes africaines, plats de riz, boissons traditionnelles, grillades'
        ),
        Poivre(
            nom='Poivre de Cayenne',
            description='En réalité un piment moulu, très piquant.',
            pays_origine='Amérique du Sud',
            intensite=9,
            utilisations='sauces piquantes, marinades, plats épicés, condiments'
        ),
        Poivre(
            nom='Poivre de Kampong',
            description='Un poivre rare avec des notes boisées et épicées.',
            pays_origine='Cambodge',
            intensite=6,
            utilisations='viandes, nouilles sautées, légumes grillés, riz frit'
        ),
        Poivre(
            nom='Poivre Sauvage de Voatsiperifery',
            description='Un poivre sauvage de Madagascar aux notes boisées et d\'agrumes.',
            pays_origine='Madagascar',
            intensite=5,
            utilisations='viandes blanches, riz parfumé, légumes, desserts au chocolat'
        ),
        Poivre(
            nom='Poivre Noir de Malabar MG1',
            description='Un poivre de haute qualité avec des grains bien mûrs et aromatiques.',
            pays_origine='Inde',
            intensite=7,
            utilisations='viandes, plats épicés, légumes grillés'
        ),
        Poivre(
            nom='Poivre Noir de Kampot IGP',
            description='Un poivre bénéficiant d\'une Indication Géographique Protégée, reconnu pour sa qualité.',
            pays_origine='Cambodge',
            intensite=6,
            utilisations='viandes, poissons, fruits de mer, légumes, plats gastronomiques'
        ),
        Poivre(
            nom='Poivre Noir de Madagascar',
            description='Un poivre aux notes chaudes et épicées avec une touche fruitée.',
            pays_origine='Madagascar',
            intensite=6,
            utilisations='viandes, légumes rôtis, sauces, fromages'
        ),
        Poivre(
            nom='Poivre Blanc de Sarawak',
            description='Un poivre blanc malaisien doux avec des notes de noisette.',
            pays_origine='Malaisie',
            intensite=5,
            utilisations='poissons, volailles, sauces blanches, purées'
        ),
        Poivre(
            nom='Poivre Noir de Kalimantan',
            description='Un poivre indonésien rare aux arômes puissants.',
            pays_origine='Indonésie',
            intensite=7,
            utilisations='viandes, plats épicés, ragoûts, currys'
        ),
        Poivre(
            nom='Poivre Rouge de Pondichéry',
            description='Un poivre rouge indien au goût fruité et épicé.',
            pays_origine='Inde',
            intensite=6,
            utilisations='volailles, fruits de mer, plats végétariens, desserts'
        ),
        Poivre(
            nom='Poivre de Madagascar Rouge',
            description='Un poivre rouge rare aux notes sucrées et épicées.',
            pays_origine='Madagascar',
            intensite=6,
            utilisations='desserts au chocolat, fruits rouges, viandes, fromages doux'
        ),
        Poivre(
            nom='Poivre de Malabar Blanc',
            description='Un poivre blanc doux et parfumé, idéal pour les plats délicats.',
            pays_origine='Inde',
            intensite=5,
            utilisations='fruits de mer, volailles, sauces légères, purées'
        ),
        Poivre(
            nom='Poivre de Rimbas',
            description='Un poivre sauvage de Bornéo aux notes fraîches et épicées.',
            pays_origine='Malaisie',
            intensite=5,
            utilisations='poissons, crevettes, légumes verts, plats asiatiques'
        ),
        Poivre(
            nom='Poivre de Phu Quoc',
            description='Un poivre vietnamien reconnu pour sa qualité supérieure.',
            pays_origine='Vietnam',
            intensite=6,
            utilisations='viandes, volailles, nouilles sautées, soupes'
        ),
        Poivre(
            nom='Poivre Noir d\'Éthiopie',
            description='Un poivre africain rare avec des notes boisées et épicées.',
            pays_origine='Éthiopie',
            intensite=6,
            utilisations='plats épicés, légumineuses, pains traditionnels'
        ),
        Poivre(
            nom='Poivre de Batak',
            description='Un poivre indonésien aux arômes d\'agrumes et de fleurs.',
            pays_origine='Indonésie',
            intensite=5,
            utilisations='poissons, fruits de mer, plats végétariens, desserts aux fruits exotiques'
        ),
        Poivre(
            nom='Poivre de Makrout',
            description='Un poivre aux notes citronnées, utilisé dans la cuisine asiatique.',
            pays_origine='Chine',
            intensite=4,
            utilisations='volailles, poissons, fruits de mer, salades, plats légers'
        ),
        Poivre(
            nom='Poivre de Cassis',
            description='Un poivre rare avec des arômes de fruits rouges.',
            pays_origine='Madagascar',
            intensite=5,
            utilisations='gibiers, viandes rouges, desserts au chocolat, sauces aux baies'
        ),
    ]

    db.session.add_all(poivres)
    db.session.commit()

print("La base de données a été mise à jour avec des utilisations culinaires moins précises pour chaque poivre.")
