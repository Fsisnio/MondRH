#!/usr/bin/env python3
"""
Script pour vérifier et créer l'utilisateur admin en production
"""

import os
import sys
import requests
from datetime import datetime

def check_admin_exists():
    """Vérifie si l'utilisateur admin existe en production"""
    print("🔍 Vérification de l'utilisateur admin en production")
    print("=" * 60)
    
    # URL de votre site en production
    production_url = "https://mondrh.onrender.com"
    
    print(f"🌐 URL: {production_url}")
    print(f"⏰ Heure: {datetime.now()}")
    print()
    
    # Test 1: Vérifier l'accessibilité du site
    print("📋 Test 1: Accessibilité du site")
    try:
        response = requests.get(production_url, timeout=30)
        if response.status_code == 200:
            print("   ✅ Site accessible")
        else:
            print(f"   ❌ Erreur {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Erreur de connexion: {e}")
        return False
    
    # Test 2: Tester la connexion avec l'email correct
    print("\n📋 Test 2: Test de connexion avec l'email correct")
    print("   📧 Email: faladespero1@gmail.com")
    print("   🔑 Mot de passe: admin124")
    
    try:
        session = requests.Session()
        
        # Données de connexion CORRECTES
        login_data = {
            'email': 'faladespero1@gmail.com',  # Email correct
            'password': 'admin124',
            'remember_me': False
        }
        
        # Tentative de connexion
        response = session.post(f"{production_url}/login", data=login_data, timeout=30)
        
        if response.status_code == 302:  # Redirection après connexion
            print("   ✅ Connexion réussie !")
            
            # Suivre la redirection
            redirect_url = response.headers.get('Location')
            if redirect_url:
                print(f"   📍 Redirection vers: {redirect_url}")
                
                # Tester l'accès au tableau de bord
                dashboard_response = session.get(f"{production_url}{redirect_url}", timeout=30)
                if dashboard_response.status_code == 200:
                    print("   ✅ Accès au tableau de bord réussi")
                    print("   🎉 L'utilisateur admin existe et fonctionne !")
                    return True
                else:
                    print(f"   ❌ Erreur d'accès au tableau de bord: {dashboard_response.status_code}")
        else:
            print(f"   ❌ Échec de la connexion: {response.status_code}")
            print(f"   📄 Réponse: {response.text[:200]}...")
            
            # Vérifier si c'est un problème d'utilisateur inexistant
            if "incorrect" in response.text.lower():
                print("   🔍 Problème: Email ou mot de passe incorrect")
                print("   💡 Cela peut signifier que l'utilisateur admin n'existe pas")
            
    except Exception as e:
        print(f"   ❌ Erreur lors du test de connexion: {e}")
    
    return False

def create_admin_via_api():
    """Tente de créer l'admin via l'API (si disponible)"""
    print("\n📋 Test 3: Tentative de création d'admin via l'API")
    
    production_url = "https://mondrh.onrender.com"
    
    try:
        # Essayer de créer un compte via l'API d'inscription
        register_data = {
            'email': 'faladespero1@gmail.com',
            'password': 'admin124',
            'first_name': 'Spero',
            'last_name': 'Falade',
            'account_type': 'admin',
            'company': 'MonDRH',
            'phone': '+33 1 23 45 67 89'
        }
        
        response = requests.post(f"{production_url}/register", data=register_data, timeout=30)
        
        if response.status_code == 302:  # Redirection après inscription
            print("   ✅ Inscription réussie !")
            return True
        else:
            print(f"   ❌ Échec de l'inscription: {response.status_code}")
            print(f"   📄 Réponse: {response.text[:200]}...")
            
    except Exception as e:
        print(f"   ❌ Erreur lors de l'inscription: {e}")
    
    return False

def main():
    """Fonction principale"""
    print("🚀 Diagnostic de l'utilisateur admin MondeRH en production")
    print("=" * 70)
    
    # Test de connexion
    if check_admin_exists():
        print("\n🎉 Résultat: L'utilisateur admin fonctionne correctement !")
        print("💡 Assurez-vous d'utiliser l'email exact: faladespero1@gmail.com")
    else:
        print("\n❌ Résultat: L'utilisateur admin n'existe pas ou ne fonctionne pas")
        print("\n🔧 Solutions:")
        print("   1. Vérifiez les logs Render pour voir si setup_production_db.py s'est exécuté")
        print("   2. Vérifiez que la base de données PostgreSQL est active")
        print("   3. Vérifiez les variables d'environnement DATABASE_URL et SECRET_KEY")
        
        # Tentative de création
        if create_admin_via_api():
            print("   ✅ Admin créé avec succès via l'API !")
        else:
            print("   ❌ Impossible de créer l'admin via l'API")
            print("\n📞 Actions à effectuer:")
            print("   1. Allez dans Render > Votre service > Logs")
            print("   2. Recherchez les erreurs de base de données")
            print("   3. Vérifiez que setup_production_db.py s'exécute au démarrage")
            print("   4. Redéployez l'application si nécessaire")

if __name__ == "__main__":
    main() 