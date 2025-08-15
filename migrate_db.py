#!/usr/bin/env python3
"""
Script de migration de base de données pour ajouter les colonnes Google
"""

import sqlite3
import os
from app import app

def migrate_database():
    """Ajoute les nouvelles colonnes pour les fonctionnalités Google"""
    
    # Chemin vers la base de données
    db_path = 'instance/monderh.db'
    if not os.path.exists(db_path):
        db_path = 'monderh.db'
    
    print(f"Migration de la base de données: {db_path}")
    
    try:
        # Connexion à la base de données
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Vérifier si les colonnes existent déjà
        print("Vérification des colonnes existantes...")
        
        # Vérifier la table application
        cursor.execute("PRAGMA table_info(application)")
        app_columns = [row[1] for row in cursor.fetchall()]
        
        # Vérifier la table appointment
        cursor.execute("PRAGMA table_info(appointment)")
        apt_columns = [row[1] for row in cursor.fetchall()]
        
        print(f"Colonnes application: {app_columns}")
        print(f"Colonnes appointment: {apt_columns}")
        
        migrations_applied = []
        
        # Ajouter google_drive_link à la table application
        if 'google_drive_link' not in app_columns:
            print("Ajout de la colonne google_drive_link à application...")
            cursor.execute("ALTER TABLE application ADD COLUMN google_drive_link VARCHAR(500)")
            migrations_applied.append("application.google_drive_link")
        else:
            print("✓ Colonne google_drive_link déjà présente dans application")
        
        # Ajouter google_calendar_link à la table appointment
        if 'google_calendar_link' not in apt_columns:
            print("Ajout de la colonne google_calendar_link à appointment...")
            cursor.execute("ALTER TABLE appointment ADD COLUMN google_calendar_link VARCHAR(500)")
            migrations_applied.append("appointment.google_calendar_link")
        else:
            print("✓ Colonne google_calendar_link déjà présente dans appointment")
        
        # Créer la table google_token si elle n'existe pas
        print("Vérification de la table google_token...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS google_token (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                access_token TEXT,
                refresh_token TEXT,
                token_uri VARCHAR(500),
                client_id VARCHAR(500),
                client_secret VARCHAR(500),
                scopes TEXT,
                expiry DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user (id)
            )
        """)
        migrations_applied.append("google_token table")
        
        # Valider les changements
        conn.commit()
        
        print(f"\n✅ Migration terminée avec succès!")
        if migrations_applied:
            print(f"Migrations appliquées: {', '.join(migrations_applied)}")
        else:
            print("Aucune migration nécessaire - base de données à jour")
        
    except Exception as e:
        print(f"❌ Erreur lors de la migration: {e}")
        conn.rollback()
    
    finally:
        conn.close()

def verify_migration():
    """Vérifie que la migration s'est bien passée"""
    print("\n🔍 Vérification de la migration...")
    
    try:
        with app.app_context():
            from app import db, Application, Appointment, GoogleToken
            
            # Test des nouvelles colonnes
            print("Test des modèles...")
            
            # Compter les applications
            app_count = Application.query.count()
            print(f"✓ Applications: {app_count}")
            
            # Compter les rendez-vous
            apt_count = Appointment.query.count()
            print(f"✓ Rendez-vous: {apt_count}")
            
            # Compter les tokens Google
            token_count = GoogleToken.query.count()
            print(f"✓ Tokens Google: {token_count}")
            
            print("✅ Vérification réussie - tous les modèles fonctionnent!")
            
    except Exception as e:
        print(f"❌ Erreur lors de la vérification: {e}")

if __name__ == '__main__':
    print("🚀 Démarrage de la migration de base de données")
    migrate_database()
    verify_migration()
    print("\n🎉 Migration terminée!") 