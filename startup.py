#!/usr/bin/env python3
"""
Script de démarrage pour s'assurer que la base de données est correctement initialisée
"""

import os
import sys
from datetime import datetime

# Ajouter le répertoire parent au path pour importer app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, JobOffer, JobApplication, User, Application, Appointment, Newsletter, SiteSettings, GoogleToken

def ensure_database_tables():
    """S'assure que toutes les tables de la base de données existent"""
    with app.app_context():
        print("🔧 Vérification de la base de données...")
        
        try:
            # Créer toutes les tables
            db.create_all()
            print("✅ Toutes les tables sont prêtes")
            
            # Vérifier que la table job_offer existe en testant une requête
            try:
                job_count = JobOffer.query.count()
                print(f"✅ Table job_offer accessible: {job_count} offres d'emploi")
            except Exception as e:
                print(f"⚠️ Table job_offer non accessible: {e}")
                # Recréer les tables si nécessaire
                db.drop_all()
                db.create_all()
                print("✅ Tables recréées avec succès")
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de la vérification de la base de données: {e}")
            return False

def add_sample_data_if_needed():
    """Ajoute des données d'exemple si les tables sont vides"""
    with app.app_context():
        try:
            # Vérifier s'il y a des offres d'emploi
            job_count = JobOffer.query.count()
            if job_count == 0:
                print("📝 Ajout d'offres d'emploi d'exemple...")
                
                sample_jobs = [
                    {
                        "title": "Responsable RH",
                        "company": "MonDRH",
                        "location": "Dakar, Sénégal",
                        "contract_type": "CDI",
                        "experience_level": "Senior",
                        "salary_range": "50000-70000€",
                        "description": "Nous recherchons un Responsable RH expérimenté pour piloter notre département Ressources Humaines et contribuer à la croissance de notre entreprise.",
                        "requirements": "• 5+ ans d'expérience en RH\n• Formation en Gestion des RH\n• Connaissance du droit social\n• Capacités managériales\n• Maîtrise des outils RH",
                        "benefits": "• Poste à responsabilités\n• Équipe dynamique\n• Formation continue\n• Avantages sociaux",
                        "department": "Ressources Humaines",
                        "is_active": True
                    },
                    {
                        "title": "Consultant en Formation",
                        "company": "MonDRH",
                        "location": "Dakar, Sénégal",
                        "contract_type": "CDD",
                        "experience_level": "Confirmé",
                        "salary_range": "35000-50000€",
                        "description": "Rejoignez notre équipe de consultants en formation pour accompagner nos clients dans le développement des compétences de leurs équipes.",
                        "requirements": "• 3+ ans d'expérience en formation\n• Certifications en formation\n• Capacités pédagogiques\n• Mobilité géographique",
                        "benefits": "• Missions variées\n• Développement professionnel\n• Travail en équipe\n• Horaires flexibles",
                        "department": "Formation",
                        "is_active": True
                    }
                ]
                
                for job_data in sample_jobs:
                    job = JobOffer(**job_data)
                    db.session.add(job)
                
                db.session.commit()
                print(f"✅ {len(sample_jobs)} offres d'emploi d'exemple ajoutées")
            else:
                print(f"✅ {job_count} offres d'emploi déjà présentes")
            
            # Vérifier s'il y a des paramètres du site
            settings_count = SiteSettings.query.count()
            if settings_count == 0:
                print("⚙️ Création des paramètres par défaut du site...")
                
                default_settings = SiteSettings(
                    site_name="MondeRH",
                    site_description="Votre partenaire en ressources humaines",
                    contact_email="contact@monderh.fr",
                    contact_phone="+33 1 23 45 67 89",
                    address="123 Avenue des Ressources Humaines, 75001 Paris",
                    hero_title="Trouvez votre carrière idéale",
                    hero_subtitle="Nous vous accompagnons dans votre parcours professionnel"
                )
                
                db.session.add(default_settings)
                db.session.commit()
                print("✅ Paramètres par défaut créés")
            else:
                print("✅ Paramètres du site déjà configurés")
                
        except Exception as e:
            print(f"⚠️ Erreur lors de l'ajout des données d'exemple: {e}")

def main():
    """Fonction principale du script de démarrage"""
    print("🚀 Démarrage de l'application MondeRH...")
    print("=" * 50)
    
    # S'assurer que les tables existent
    if ensure_database_tables():
        # Ajouter des données d'exemple si nécessaire
        add_sample_data_if_needed()
        print("\n🎉 Application prête à démarrer !")
        return True
    else:
        print("\n❌ Erreur lors de l'initialisation de la base de données")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 