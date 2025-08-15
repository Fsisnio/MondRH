#!/usr/bin/env python3
"""
Script pour vérifier l'état de l'authentification admin
"""

import requests
import json
from urllib.parse import urljoin

def check_auth_status():
    """Vérifier l'état de l'authentification"""
    
    base_url = "http://10.188.193.170:5000"
    
    print("🔍 Vérification de l'état d'authentification")
    print("=" * 60)
    
    # Créer une session pour maintenir les cookies
    session = requests.Session()
    
    # Test 1: Vérifier la page de login
    print("\n1. Test de la page de login...")
    try:
        response = session.get(f"{base_url}/login", timeout=10)
        print(f"   Status: {response.status_code}")
        print(f"   URL: {response.url}")
        
        if response.status_code == 200:
            print("   ✅ Page de login accessible")
        else:
            print(f"   ❌ Erreur: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Erreur de connexion: {e}")
        return
    
    # Test 2: Tentative de connexion admin
    print("\n2. Tentative de connexion admin...")
    
    login_data = {
        'email': 'admin@monderh.fr',
        'password': 'admin123'
    }
    
    try:
        response = session.post(f"{base_url}/login", data=login_data, timeout=10, allow_redirects=True)
        print(f"   Status: {response.status_code}")
        print(f"   URL finale: {response.url}")
        
        if response.status_code == 200:
            if "admin" in response.url or "dashboard" in response.url:
                print("   ✅ Connexion réussie")
            elif "login" in response.url:
                print("   ❌ Connexion échouée - resté sur la page login")
            else:
                print("   ⚠️  Connexion - URL inattendue")
        elif response.status_code == 302:
            print("   ✅ Redirection après connexion")
            print(f"   Location: {response.headers.get('Location', 'Non spécifiée')}")
        else:
            print(f"   ❌ Erreur: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Erreur de connexion: {e}")
    
    # Test 3: Vérifier l'accès à la page admin
    print("\n3. Test d'accès à la page admin...")
    try:
        response = session.get(f"{base_url}/admin", timeout=10)
        print(f"   Status: {response.status_code}")
        print(f"   URL: {response.url}")
        
        if response.status_code == 200:
            if "admin" in response.url:
                print("   ✅ Accès admin autorisé")
            else:
                print("   ⚠️  Accès admin - URL inattendue")
        elif response.status_code == 302:
            print("   ❌ Redirection - accès non autorisé")
            print(f"   Location: {response.headers.get('Location', 'Non spécifiée')}")
        else:
            print(f"   ❌ Erreur: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Erreur d'accès: {e}")
    
    # Test 4: Vérifier l'accès au formulaire de création d'offre
    print("\n4. Test d'accès au formulaire de création d'offre...")
    try:
        response = session.get(f"{base_url}/admin/jobs/new", timeout=10)
        print(f"   Status: {response.status_code}")
        print(f"   URL: {response.url}")
        
        if response.status_code == 200:
            if "admin/jobs/new" in response.url:
                print("   ✅ Accès au formulaire autorisé")
                # Vérifier le contenu
                if "Debug Info" in response.text:
                    print("   ✅ Formulaire simplifié trouvé")
                else:
                    print("   ❌ Formulaire simplifié non trouvé")
            else:
                print("   ⚠️  Accès au formulaire - URL inattendue")
        elif response.status_code == 302:
            print("   ❌ Redirection - accès non autorisé")
            print(f"   Location: {response.headers.get('Location', 'Non spécifiée')}")
        else:
            print(f"   ❌ Erreur: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Erreur d'accès: {e}")
    
    # Test 5: Vérifier les cookies de session
    print("\n5. Vérification des cookies de session...")
    cookies = session.cookies
    if cookies:
        print("   ✅ Cookies de session présents:")
        for cookie in cookies:
            print(f"     {cookie.name}: {cookie.value[:20]}...")
    else:
        print("   ❌ Aucun cookie de session")
    
    print("\n" + "=" * 60)
    print("🔧 Recommandations:")
    print("1. Vérifiez que vous êtes bien connecté en tant qu'admin")
    print("2. Essayez de vous reconnecter")
    print("3. Vérifiez que l'utilisateur admin existe dans la base de données")
    print("4. Testez avec le formulaire de test: /test/jobs/form")

if __name__ == "__main__":
    check_auth_status() 