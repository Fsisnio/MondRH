#!/usr/bin/env python3
"""
Script d'initialisation de la base de données pour MonDRH
"""

import os
import sys
from datetime import datetime

# Ajouter le répertoire parent au path pour importer app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, JobOffer, Newsletter

def init_database():
    """Initialise la base de données et crée les tables"""
    with app.app_context():
        print("🔧 Initialisation de la base de données...")
        
        try:
            # Créer toutes les tables
            db.create_all()
            print("✅ Tables créées avec succès !")
            
            # Vérifier si un utilisateur admin existe
            admin_user = User.query.filter_by(user_type='admin').first()
            if not admin_user:
                print("👤 Création d'un utilisateur administrateur...")
                admin_user = User(
                    email='admin@monderh.fr',
                    password_hash='pbkdf2:sha256:600000$dev-admin-password-hash',
                    first_name='Admin',
                    last_name='MonDRH',
                    user_type='admin',
                    company='MonDRH',
                    phone='+33 1 23 45 67 89'
                )
                db.session.add(admin_user)
                db.session.commit()
                print("✅ Utilisateur administrateur créé !")
                print("   Email: admin@monderh.fr")
                print("   Mot de passe: admin123")
            else:
                print("✅ Utilisateur administrateur existe déjà")
            
            # Vérifier le nombre d'offres d'emploi
            job_count = JobOffer.query.count()
            print(f"📋 {job_count} offres d'emploi dans la base de données")
            
            # Vérifier le nombre d'abonnés newsletter
            newsletter_count = Newsletter.query.count()
            print(f"📧 {newsletter_count} abonnés à la newsletter")
            
            print("\n🎉 Initialisation terminée avec succès !")
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de l'initialisation: {e}")
            return False

if __name__ == "__main__":
    print("🚀 Initialisation de la base de données - MonDRH")
    print("=" * 50)
    
    if init_database():
        print("\n📱 Vous pouvez maintenant :")
        print("   1. Accéder à l'application")
        print("   2. Vous connecter avec admin@monderh.fr")
        print("   3. Gérer les offres d'emploi et les utilisateurs")
    else:
        print("\n❌ Initialisation échouée !")
        sys.exit(1) 