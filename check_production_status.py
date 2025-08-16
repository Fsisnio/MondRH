#!/usr/bin/env python3
"""
Script de diagnostic pour vérifier la configuration de production
"""

import os
import sys
import logging
from datetime import datetime

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_environment_variables():
    """Vérifie les variables d'environnement critiques"""
    logger.info("🔍 Vérification des variables d'environnement...")
    
    critical_vars = [
        'DATABASE_URL',
        'SECRET_KEY',
        'FLASK_ENV',
        'FLASK_DEBUG'
    ]
    
    optional_vars = [
        'MAIL_USERNAME',
        'MAIL_PASSWORD',
        'GOOGLE_CLIENT_ID',
        'GOOGLE_CLIENT_SECRET'
    ]
    
    print("\n📋 Variables d'environnement critiques:")
    for var in critical_vars:
        value = os.environ.get(var)
        if value:
            if var == 'DATABASE_URL':
                # Masquer l'URL de la base de données pour la sécurité
                masked_value = value[:20] + "..." if len(value) > 20 else value
                print(f"   ✅ {var}: {masked_value}")
            else:
                print(f"   ✅ {var}: {value}")
        else:
            print(f"   ❌ {var}: NON DÉFINIE")
    
    print("\n📋 Variables d'environnement optionnelles:")
    for var in optional_vars:
        value = os.environ.get(var)
        if value:
            print(f"   ✅ {var}: {value}")
        else:
            print(f"   ⚠️  {var}: NON DÉFINIE (optionnel)")

def check_database_connection():
    """Vérifie la connexion à la base de données"""
    logger.info("🔍 Vérification de la connexion à la base de données...")
    
    try:
        # Importer app et db
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from app import app, db
        
        with app.app_context():
            # Tester la connexion
            db.session.execute('SELECT 1')
            print("   ✅ Connexion à la base de données réussie")
            
            # Vérifier les tables
            from app import User, Application, Appointment, JobOffer
            tables = [User, Application, Appointment, JobOffer]
            
            for table in tables:
                try:
                    count = table.query.count()
                    print(f"   ✅ Table {table.__name__}: {count} enregistrements")
                except Exception as e:
                    print(f"   ❌ Erreur avec la table {table.__name__}: {e}")
                    
    except Exception as e:
        print(f"   ❌ Erreur de connexion à la base de données: {e}")

def check_admin_users():
    """Vérifie les utilisateurs administrateurs"""
    logger.info("🔍 Vérification des utilisateurs administrateurs...")
    
    try:
        from app import app, db, User
        
        with app.app_context():
            admins = User.query.filter_by(user_type='admin').all()
            
            if admins:
                print(f"   ✅ {len(admins)} utilisateur(s) administrateur(s) trouvé(s):")
                for admin in admins:
                    print(f"      • {admin.email} ({admin.first_name} {admin.last_name}) - Actif: {admin.is_active}")
            else:
                print("   ❌ Aucun utilisateur administrateur trouvé")
                
    except Exception as e:
        print(f"   ❌ Erreur lors de la vérification des admins: {e}")

def check_file_permissions():
    """Vérifie les permissions des fichiers"""
    logger.info("🔍 Vérification des permissions des fichiers...")
    
    critical_files = [
        'app.py',
        'config.py',
        'requirements.txt',
        'static/uploads'
    ]
    
    for file_path in critical_files:
        if os.path.exists(file_path):
            if os.access(file_path, os.R_OK):
                print(f"   ✅ {file_path}: Lisible")
            else:
                print(f"   ❌ {file_path}: Non lisible")
                
            if os.path.isfile(file_path):
                if os.access(file_path, os.W_OK):
                    print(f"   ✅ {file_path}: Modifiable")
                else:
                    print(f"   ⚠️  {file_path}: Non modifiable")
        else:
            print(f"   ❌ {file_path}: N'existe pas")

def check_python_environment():
    """Vérifie l'environnement Python"""
    logger.info("🔍 Vérification de l'environnement Python...")
    
    print(f"   ✅ Version Python: {sys.version}")
    print(f"   ✅ Répertoire de travail: {os.getcwd()}")
    print(f"   ✅ Variables d'environnement PATH: {len(os.environ.get('PATH', '').split(':'))} répertoires")

def check_requirements():
    """Vérifie les dépendances Python"""
    logger.info("🔍 Vérification des dépendances...")
    
    try:
        import flask
        print(f"   ✅ Flask: {flask.__version__}")
    except ImportError:
        print("   ❌ Flask: Non installé")
    
    try:
        import flask_sqlalchemy
        print(f"   ✅ Flask-SQLAlchemy: {flask_sqlalchemy.__version__}")
    except ImportError:
        print("   ❌ Flask-SQLAlchemy: Non installé")
    
    try:
        import flask_login
        print(f"   ✅ Flask-Login: Installé")
    except ImportError:
        print("   ❌ Flask-Login: Non installé")

def main():
    """Fonction principale"""
    print("🚀 Diagnostic de la configuration de production MondeRH")
    print("=" * 60)
    print(f"📅 Date et heure: {datetime.now()}")
    print(f"🌍 Environnement: {os.environ.get('FLASK_ENV', 'Non défini')}")
    print("=" * 60)
    
    check_environment_variables()
    print()
    
    check_python_environment()
    print()
    
    check_requirements()
    print()
    
    check_file_permissions()
    print()
    
    check_database_connection()
    print()
    
    check_admin_users()
    print()
    
    print("=" * 60)
    print("🎯 Recommandations:")
    print("   1. Vérifiez que DATABASE_URL est correctement configurée")
    print("   2. Assurez-vous que SECRET_KEY est définie et sécurisée")
    print("   3. Vérifiez que FLASK_ENV=production")
    print("   4. Assurez-vous qu'au moins un utilisateur admin existe")
    print("   5. Vérifiez les logs de l'application pour plus de détails")

if __name__ == "__main__":
    main() 