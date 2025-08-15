#!/usr/bin/env python3
"""
Script pour corriger la structure de la base de données
Ajoute les colonnes manquantes à la table application
"""

import sqlite3
import os

def fix_database():
    db_path = 'instance/monderh.db'
    
    if not os.path.exists(db_path):
        print(f"Base de données non trouvée: {db_path}")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Vérifier si la colonne job_offer_id existe
        cursor.execute("PRAGMA table_info(application)")
        columns = [column[1] for column in cursor.fetchall()]
        
        print("Colonnes actuelles dans la table application:")
        for col in columns:
            print(f"  - {col}")
        
        # Ajouter la colonne job_offer_id si elle n'existe pas
        if 'job_offer_id' not in columns:
            print("\nAjout de la colonne job_offer_id...")
            cursor.execute("""
                ALTER TABLE application 
                ADD COLUMN job_offer_id INTEGER 
                REFERENCES job_offer(id)
            """)
            print("✓ Colonne job_offer_id ajoutée")
        else:
            print("\n✓ Colonne job_offer_id existe déjà")
        
        # Vérifier si la colonne google_drive_link existe
        if 'google_drive_link' not in columns:
            print("\nAjout de la colonne google_drive_link...")
            cursor.execute("""
                ALTER TABLE application 
                ADD COLUMN google_drive_link VARCHAR(500)
            """)
            print("✓ Colonne google_drive_link ajoutée")
        else:
            print("\n✓ Colonne google_drive_link existe déjà")
        
        # Vérifier la structure finale
        cursor.execute("PRAGMA table_info(application)")
        final_columns = [column[1] for column in cursor.fetchall()]
        
        print("\nStructure finale de la table application:")
        for col in final_columns:
            print(f"  - {col}")
        
        conn.commit()
        print("\n✓ Base de données mise à jour avec succès!")
        
    except Exception as e:
        print(f"Erreur lors de la mise à jour: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    fix_database() 