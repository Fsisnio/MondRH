# Configuration Google OAuth pour MonDRH
# Fichier de configuration pour l'intégration Google Workspace

import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# Configuration OAuth 2.0
GOOGLE_CLIENT_CONFIG = {
    "web": {
        "client_id": os.environ.get('GOOGLE_CLIENT_ID') or "your-google-client-id-here",
        "client_secret": os.environ.get('GOOGLE_CLIENT_SECRET') or "your-google-client-secret-here",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "redirect_uris": [
            "http://localhost:5000/auth/google/callback",
            "https://monderh.onrender.com/auth/google/callback"
        ]
    }
}

# Scopes nécessaires pour l'application
SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

def create_credentials_file():
    """Crée le fichier credentials.json pour Google OAuth"""
    import json
    
    credentials_data = {
        "installed": {
            "client_id": GOOGLE_CLIENT_CONFIG["web"]["client_id"],
            "client_secret": GOOGLE_CLIENT_CONFIG["web"]["client_secret"],
            "auth_uri": GOOGLE_CLIENT_CONFIG["web"]["auth_uri"],
            "token_uri": GOOGLE_CLIENT_CONFIG["web"]["token_uri"],
            "auth_provider_x509_cert_url": GOOGLE_CLIENT_CONFIG["web"]["auth_provider_x509_cert_url"],
            "redirect_uris": GOOGLE_CLIENT_CONFIG["web"]["redirect_uris"]
        }
    }
    
    with open('credentials.json', 'w') as f:
        json.dump(credentials_data, f, indent=2)
    
    print("✅ Fichier credentials.json créé avec succès!")

def get_google_credentials():
    """Récupère les credentials Google OAuth"""
    creds = None
    
    # Le fichier token.pickle contient les tokens d'accès et de rafraîchissement
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Si les credentials n'existent pas ou sont invalides
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Sauvegarde les credentials pour la prochaine exécution
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def test_google_connection():
    """Teste la connexion Google"""
    try:
        from googleapiclient.discovery import build
        
        creds = get_google_credentials()
        service = build('drive', 'v3', credentials=creds)
        
        # Test simple - récupère les informations sur l'utilisateur
        about = service.about().get(fields="user").execute()
        user_info = about.get('user', {})
        
        print("✅ Connexion Google réussie!")
        print(f"👤 Utilisateur connecté: {user_info.get('displayName', 'Inconnu')}")
        print(f"📧 Email: {user_info.get('emailAddress', 'Non disponible')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur de connexion Google: {e}")
        return False

def setup_google_workspace():
    """Configure complètement Google Workspace"""
    print("🚀 Configuration de Google Workspace pour MonDRH...")
    
    # 1. Créer le fichier credentials
    create_credentials_file()
    
    # 2. Tester la connexion
    print("\n🔗 Test de la connexion Google...")
    if test_google_connection():
        print("\n✅ Google Workspace configuré avec succès!")
        return True
    else:
        print("\n❌ Échec de la configuration Google Workspace")
        return False

if __name__ == "__main__":
    setup_google_workspace() 