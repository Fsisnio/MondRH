#!/usr/bin/env python3
"""
Script pour créer un utilisateur administrateur
Usage: python create_admin.py
"""

from app import app, db, User
from werkzeug.security import generate_password_hash

def create_admin():
    with app.app_context():
        # Vérifier si un admin existe déjà
        existing_admin = User.query.filter_by(user_type='admin').first()
        if existing_admin:
            print(f"Un administrateur existe déjà: {existing_admin.email}")
            return

        # Créer l'administrateur
        admin_email = input("Email de l'administrateur: ")
        admin_password = input("Mot de passe de l'administrateur: ")
        admin_first_name = input("Prénom: ")
        admin_last_name = input("Nom: ")

        admin_user = User(
            email=admin_email,
            password_hash=generate_password_hash(admin_password),
            first_name=admin_first_name,
            last_name=admin_last_name,
            user_type='admin',
            is_active=True
        )

        db.session.add(admin_user)
        db.session.commit()

        print(f"Administrateur créé avec succès: {admin_email}")
        print("Vous pouvez maintenant vous connecter avec ces identifiants.")

if __name__ == '__main__':
    create_admin() 