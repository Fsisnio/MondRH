#!/usr/bin/env python3
"""
Script de diagnostic pour les comptes administrateurs
"""

import os
import sys
from datetime import datetime

# Ajouter le répertoire parent au path pour importer app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User

def check_admin_users():
    """Vérifie l'état des comptes administrateurs"""
    with app.app_context():
        print("🔍 Diagnostic des comptes administrateurs...")
        print("=" * 50)
        
        try:
            # Vérifier la connexion à la base de données
            db.session.execute('SELECT 1')
            print("✅ Connexion à la base de données réussie")
            
            # Compter tous les utilisateurs
            total_users = User.query.count()
            print(f"📊 Total utilisateurs: {total_users}")
            
            # Vérifier les administrateurs
            admin_users = User.query.filter_by(user_type='admin').all()
            print(f"👑 Utilisateurs administrateurs: {len(admin_users)}")
            
            if admin_users:
                print("\n📋 Détails des administrateurs:")
                for i, admin in enumerate(admin_users, 1):
                    print(f"  {i}. {admin.email}")
                    print(f"     Nom: {admin.first_name} {admin.last_name}")
                    print(f"     Type: {admin.user_type}")
                    print(f"     Actif: {admin.is_active}")
                    print(f"     Créé le: {admin.created_at}")
                    print(f"     Hash du mot de passe: {admin.password_hash[:50]}...")
                    print()
            else:
                print("❌ Aucun administrateur trouvé !")
                
                # Vérifier s'il y a des utilisateurs avec d'autres types
                other_users = User.query.filter(User.user_type != 'admin').all()
                if other_users:
                    print("\n👥 Autres utilisateurs trouvés:")
                    for user in other_users:
                        print(f"  - {user.email} (type: {user.user_type})")
                
                print("\n🔧 Solutions possibles:")
                print("  1. Exécuter: python setup_production_db.py")
                print("  2. Exécuter: python init_db.py")
                print("  3. Créer manuellement un admin via l'interface")
            
            # Vérifier la structure de la table User
            print("\n🏗️ Structure de la table User:")
            user_columns = User.__table__.columns
            for column in user_columns:
                print(f"  - {column.name}: {column.type}")
            
            return len(admin_users) > 0
            
        except Exception as e:
            print(f"❌ Erreur lors du diagnostic: {e}")
            return False

def create_admin_user():
    """Crée un utilisateur administrateur"""
    with app.app_context():
        print("\n🔧 Création d'un utilisateur administrateur...")
        
        try:
            # Vérifier s'il y a déjà un admin
            existing_admin = User.query.filter_by(email='admin@monderh.fr').first()
            if existing_admin:
                print("⚠️ Un administrateur avec cet email existe déjà")
                if existing_admin.user_type == 'admin':
                    print("✅ Le compte est déjà configuré comme administrateur")
                    return True
                else:
                    print(f"⚠️ Le compte existe mais n'est pas admin (type: {existing_admin.user_type})")
                    # Mettre à jour le type
                    existing_admin.user_type = 'admin'
                    db.session.commit()
                    print("✅ Type d'utilisateur mis à jour vers 'admin'")
                    return True
            
            # Créer un nouvel administrateur
            from werkzeug.security import generate_password_hash
            
            admin_user = User(
                email='admin@monderh.fr',
                password_hash=generate_password_hash('admin123'),
                first_name='Admin',
                last_name='MonDRH',
                user_type='admin',
                is_active=True
            )
            
            db.session.add(admin_user)
            db.session.commit()
            
            print("✅ Nouvel administrateur créé avec succès:")
            print("   Email: admin@monderh.fr")
            print("   Mot de passe: admin123")
            print("   Type: admin")
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de la création: {e}")
            db.session.rollback()
            return False

def test_admin_login():
    """Teste la connexion administrateur"""
    with app.app_context():
        print("\n🔐 Test de connexion administrateur...")
        
        try:
            from werkzeug.security import check_password_hash
            
            admin = User.query.filter_by(email='admin@monderh.fr').first()
            if not admin:
                print("❌ Aucun administrateur trouvé")
                return False
            
            if admin.user_type != 'admin':
                print(f"❌ L'utilisateur n'est pas administrateur (type: {admin.user_type})")
                return False
            
            # Tester le mot de passe
            test_password = 'admin123'
            if check_password_hash(admin.password_hash, test_password):
                print("✅ Mot de passe correct")
                print("✅ Compte administrateur fonctionnel")
                return True
            else:
                print("❌ Mot de passe incorrect")
                print("🔧 Le hash du mot de passe ne correspond pas")
                return False
                
        except Exception as e:
            print(f"❌ Erreur lors du test: {e}")
            return False

def main():
    """Fonction principale"""
    print("🚀 Diagnostic des comptes administrateurs - MonDRH")
    print("=" * 60)
    
    # Vérifier l'état actuel
    has_admin = check_admin_users()
    
    if not has_admin:
        print("\n🔧 Création d'un administrateur...")
        if create_admin_user():
            print("✅ Administrateur créé avec succès")
        else:
            print("❌ Échec de la création de l'administrateur")
            return False
    
    # Tester la connexion
    if test_admin_login():
        print("\n🎉 Diagnostic terminé avec succès !")
        print("✅ Les comptes administrateurs fonctionnent correctement")
        return True
    else:
        print("\n❌ Problème détecté avec les comptes administrateurs")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 