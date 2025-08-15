#!/usr/bin/env python3
"""
Script de vérification de la configuration Google OAuth
"""

import os
from dotenv import load_dotenv

def check_google_config():
    """Vérifie la configuration Google OAuth"""
    print("🔍 Vérification de la configuration Google OAuth...")
    print("=" * 50)
    
    # Charger les variables d'environnement
    load_dotenv()
    
    # Vérifier les variables
    client_id = os.getenv('GOOGLE_CLIENT_ID')
    client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
    
    print(f"📁 Fichier .env : {'✅ Trouvé' if os.path.exists('.env') else '❌ Non trouvé'}")
    print(f"🔑 GOOGLE_CLIENT_ID : {'✅ Configuré' if client_id else '❌ Manquant'}")
    print(f"🔐 GOOGLE_CLIENT_SECRET : {'✅ Configuré' if client_secret else '❌ Manquant'}")
    
    if client_id and client_secret:
        print("\n✅ Configuration Google OAuth complète !")
        print("Vous pouvez maintenant utiliser l'intégration Google Workspace.")
        
        # Vérifier le format du CLIENT_ID
        if client_id.endswith('.apps.googleusercontent.com'):
            print("✅ Format du CLIENT_ID correct")
        else:
            print("⚠️  Format du CLIENT_ID suspect")
            
    else:
        print("\n❌ Configuration Google OAuth incomplète !")
        print("\n📋 Pour configurer Google OAuth :")
        print("1. Suivez le guide dans GOOGLE_SETUP_GUIDE.md")
        print("2. Créez un fichier .env à la racine du projet")
        print("3. Ajoutez vos clés Google OAuth :")
        print("   GOOGLE_CLIENT_ID=votre-client-id.apps.googleusercontent.com")
        print("   GOOGLE_CLIENT_SECRET=votre-client-secret")
        print("4. Redémarrez l'application")
    
    print("\n" + "=" * 50)

if __name__ == '__main__':
    check_google_config() 