#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🚀 Début du build MonDRH..."

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# Créer le dossier uploads s'il n'existe pas
echo "📁 Création du dossier uploads..."
mkdir -p static/uploads

# Initialiser la base de données et créer les administrateurs
echo "🗄️ Configuration de la base de données PostgreSQL..."
python setup_production_db.py

echo "✅ Build terminé avec succès!" 