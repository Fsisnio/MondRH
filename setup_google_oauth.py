#!/usr/bin/env python3
"""
Script interactif pour configurer Google OAuth
"""

import os
import re

def setup_google_oauth():
    """Configure Google OAuth de manière interactive"""
    print("🔧 Configuration Google OAuth - MonDRH")
    print("=" * 50)
    print()
    print("📋 Ce script vous aide à configurer l'intégration Google Workspace.")
    print("Vous devez d'abord créer un projet Google Cloud et obtenir vos clés OAuth.")
    print()
    print("📖 Consultez le guide complet : GOOGLE_SETUP_GUIDE.md")
    print()
    
    # Vérifier si .env existe
    if os.path.exists('.env'):
        print("⚠️  Le fichier .env existe déjà.")
        overwrite = input("Voulez-vous le remplacer ? (y/N): ").lower()
        if overwrite != 'y':
            print("❌ Configuration annulée.")
            return
    
    print("🔑 Entrez vos clés Google OAuth :")
    print()
    
    # Demander le CLIENT_ID
    while True:
        client_id = input("GOOGLE_CLIENT_ID: ").strip()
        if not client_id:
            print("❌ Le CLIENT_ID est requis.")
            continue
        if not client_id.endswith('.apps.googleusercontent.com'):
            print("⚠️  Le CLIENT_ID doit se terminer par .apps.googleusercontent.com")
            continue
        break
    
    # Demander le CLIENT_SECRET
    while True:
        client_secret = input("GOOGLE_CLIENT_SECRET: ").strip()
        if not client_secret:
            print("❌ Le CLIENT_SECRET est requis.")
            continue
        break
    
    # Demander la clé secrète Flask
    secret_key = input("SECRET_KEY (optionnel, appuyez sur Entrée pour générer): ").strip()
    if not secret_key:
        import secrets
        secret_key = secrets.token_hex(32)
        print(f"🔐 Clé secrète générée : {secret_key[:16]}...")
    
    # Créer le contenu du fichier .env
    env_content = f"""# Configuration Google OAuth
GOOGLE_CLIENT_ID={client_id}
GOOGLE_CLIENT_SECRET={client_secret}

# Configuration Email (optionnel)
MAIL_USERNAME=contact@monderh.fr
MAIL_PASSWORD=your-email-password

# Clé secrète Flask
SECRET_KEY={secret_key}

# Configuration de la base de données (optionnel)
# SQLALCHEMY_DATABASE_URI=sqlite:///monderh.db

# Configuration du serveur (optionnel)
# FLASK_ENV=development
# FLASK_DEBUG=True
"""
    
    # Écrire le fichier .env
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print()
        print("✅ Fichier .env créé avec succès !")
        print()
        print("📋 Prochaines étapes :")
        print("1. Redémarrez l'application Flask")
        print("2. Connectez-vous à votre compte")
        print("3. Testez l'intégration Google Workspace")
        print()
        print("🔍 Pour vérifier la configuration :")
        print("   python check_google_config.py")
        
    except Exception as e:
        print(f"❌ Erreur lors de la création du fichier .env : {e}")

if __name__ == '__main__':
    setup_google_oauth() 