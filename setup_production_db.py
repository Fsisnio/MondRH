#!/usr/bin/env python3
"""
Script de configuration de la base de données de production pour Render
"""

import os
import sys
from datetime import datetime
import psycopg2
from urllib.parse import urlparse

# Ajouter le répertoire parent au path pour importer app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, JobOffer, Application, Appointment, Newsletter, SiteSettings, GoogleToken

def setup_production_database():
    """Configure la base de données de production"""
    with app.app_context():
        print("🔧 Configuration de la base de données de production...")
        
        try:
            # Vérifier la variable d'environnement DATABASE_URL
            database_url = os.environ.get('DATABASE_URL')
            if not database_url:
                print("❌ Variable d'environnement DATABASE_URL non trouvée")
                return False
            
            print(f"✅ URL de base de données détectée: {database_url[:20]}...")
            
            # Créer toutes les tables
            db.create_all()
            print("✅ Toutes les tables créées avec succès")
            
            # Vérifier la connexion
            try:
                db.session.execute('SELECT 1')
                print("✅ Connexion à la base de données réussie")
            except Exception as e:
                print(f"❌ Erreur de connexion: {e}")
                return False
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de la configuration: {e}")
            return False

def create_admin_user():
    """Crée un utilisateur administrateur par défaut"""
    with app.app_context():
        try:
            # Vérifier s'il y a déjà un admin
            admin = User.query.filter_by(email='admin@monderh.fr').first()
            if admin:
                print("✅ Utilisateur administrateur déjà existant")
                return True
            
            # Créer l'admin par défaut
            from werkzeug.security import generate_password_hash
            
            admin_user = User(
                email='faladespero1@gmail.com',
                password_hash=generate_password_hash('admin124'),
                first_name='Spero',
                last_name='Falade',
                user_type='admin',
                is_active=True
            )
            
            db.session.add(admin_user)
            db.session.commit()
            
            print("✅ Utilisateur administrateur créé:")
            print("   Email: faladespero1@gmail.com")
            print("   Mot de passe: admin124")
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de la création de l'admin: {e}")
            return False

def add_sample_data():
    """Ajoute des données d'exemple pour la production"""
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
    """Fonction principale"""
    print("🚀 Configuration de la base de données de production...")
    print("=" * 60)
    
    # Configuration de la base de données
    if not setup_production_database():
        print("❌ Échec de la configuration de la base de données")
        return False
    
    # Création de l'utilisateur admin
    if not create_admin_user():
        print("❌ Échec de la création de l'utilisateur admin")
        return False
    
    # Ajout des données d'exemple
    add_sample_data()
    
    print("\n🎉 Configuration de production terminée avec succès !")
    print("=" * 60)
    print("📋 Informations importantes:")
    print("   • URL de l'application: https://votre-app.onrender.com")
    print("   • Email admin: faladespero1@gmail.com")
    print("   • Mot de passe admin: admin124")
    print("   • N'oubliez pas de changer le mot de passe admin !")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 