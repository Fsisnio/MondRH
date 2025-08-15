# Configuration MonDRH
import os

class Config:
    # Configuration de base
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'monderh-secret-key-2024-production-super-secure-12345'
    
    # Configuration Email
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'contact@monderh.fr'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'votre-mot-de-passe-email-app'
    
    # Configuration Google OAuth
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID') or 'your-google-client-id-here'
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') or 'your-google-client-secret-here'
    
    # Configuration Base de Données
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///monderh.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuration Flask
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG') or True

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'

# Configuration par défaut
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 