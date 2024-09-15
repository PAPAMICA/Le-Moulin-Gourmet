# Utiliser une image de base Python
FROM python:3.12-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances de l'application
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Définir la commande de démarrage
CMD ["flask", "run", "--host=0.0.0.0"]