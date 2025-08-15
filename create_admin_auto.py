#!/usr/bin/env python3
"""
Script automatisé pour créer un utilisateur administrateur de test
"""

from app import app, db, User
from werkzeug.security import generate_password_hash

def create_admin_auto():
    with app.app_context():
        # Vérifier si un admin existe déjà
        existing_admin = User.query.filter_by(user_type='admin').first()
        if existing_admin:
            print(f"Un administrateur existe déjà: {existing_admin.email}")
            return

        # Créer l'administrateur avec des données par défaut
        admin_user = User(
            email='admin@monderh.fr',
            password_hash=generate_password_hash('admin123'),
            first_name='Admin',
            last_name='MondeRH',
            user_type='admin',
            is_active=True
        )

        db.session.add(admin_user)
        db.session.commit()

        print("Administrateur créé avec succès!")
        print("Email: admin@monderh.fr")
        print("Mot de passe: admin123")
        print("Vous pouvez maintenant vous connecter avec ces identifiants.")

if __name__ == '__main__':
    create_admin_auto() 