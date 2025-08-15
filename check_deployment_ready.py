#!/usr/bin/env python3
"""
Script de vérification pour le déploiement Render
"""

import os
import sys
from pathlib import Path

def check_required_files():
    """Vérifie que tous les fichiers requis sont présents"""
    print("🔍 Vérification des fichiers requis...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        'render.yaml',
        'setup_production_db.py',
        'build.sh',
        'config.py',
        '.gitignore'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✅ {file}")
    
    if missing_files:
        print(f"❌ Fichiers manquants: {missing_files}")
        return False
    
    print("✅ Tous les fichiers requis sont présents")
    return True

def check_requirements():
    """Vérifie le fichier requirements.txt"""
    print("\n📦 Vérification de requirements.txt...")
    
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read()
        
        # Vérifier les dépendances critiques
        critical_deps = [
            'Flask',
            'gunicorn',
            'psycopg2-binary',
            'Flask-SQLAlchemy'
        ]
        
        missing_deps = []
        for dep in critical_deps:
            if dep not in requirements:
                missing_deps.append(dep)
            else:
                print(f"✅ {dep}")
        
        if missing_deps:
            print(f"❌ Dépendances manquantes: {missing_deps}")
            return False
        
        print("✅ Toutes les dépendances critiques sont présentes")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la vérification de requirements.txt: {e}")
        return False

def check_config():
    """Vérifie la configuration"""
    print("\n⚙️ Vérification de la configuration...")
    
    try:
        # Vérifier que l'application peut être importée
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from app import app
        
        print("✅ Application Flask importée avec succès")
        
        # Vérifier les variables de configuration
        config = app.config
        
        required_configs = [
            'SECRET_KEY',
            'SQLALCHEMY_DATABASE_URI',
            'MAIL_USERNAME'
        ]
        
        missing_configs = []
        for config_key in required_configs:
            if not config.get(config_key):
                missing_configs.append(config_key)
            else:
                print(f"✅ {config_key} configuré")
        
        if missing_configs:
            print(f"⚠️ Configurations manquantes (seront définies par les variables d'environnement): {missing_configs}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la vérification de la configuration: {e}")
        return False

def check_directories():
    """Vérifie que les dossiers nécessaires existent"""
    print("\n📁 Vérification des dossiers...")
    
    required_dirs = [
        'static',
        'static/uploads',
        'templates',
        'templates/admin'
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
        else:
            print(f"✅ {dir_path}")
    
    if missing_dirs:
        print(f"❌ Dossiers manquants: {missing_dirs}")
        return False
    
    print("✅ Tous les dossiers requis sont présents")
    return True

def check_gitignore():
    """Vérifie que le .gitignore exclut les fichiers sensibles"""
    print("\n🚫 Vérification du .gitignore...")
    
    try:
        with open('.gitignore', 'r') as f:
            gitignore_content = f.read()
        
        sensitive_patterns = [
            '*.db',
            'instance/',
            'venv/',
            '.env',
            '__pycache__/',
            '*.pyc'
        ]
        
        missing_patterns = []
        for pattern in sensitive_patterns:
            if pattern not in gitignore_content:
                missing_patterns.append(pattern)
            else:
                print(f"✅ {pattern} exclu")
        
        if missing_patterns:
            print(f"⚠️ Patterns manquants dans .gitignore: {missing_patterns}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la vérification du .gitignore: {e}")
        return False

def check_render_config():
    """Vérifie la configuration Render"""
    print("\n🌐 Vérification de la configuration Render...")
    
    try:
        with open('render.yaml', 'r') as f:
            render_config = f.read()
        
        required_elements = [
            'type: web',
            'env: python',
            'buildCommand:',
            'startCommand:',
            'gunicorn',
            'setup_production_db.py'
        ]
        
        missing_elements = []
        for element in required_elements:
            if element not in render_config:
                missing_elements.append(element)
            else:
                print(f"✅ {element}")
        
        if missing_elements:
            print(f"❌ Éléments manquants dans render.yaml: {missing_elements}")
            return False
        
        print("✅ Configuration Render valide")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la vérification de render.yaml: {e}")
        return False

def main():
    """Fonction principale"""
    print("🚀 Vérification de préparation au déploiement Render")
    print("=" * 60)
    
    checks = [
        check_required_files,
        check_requirements,
        check_config,
        check_directories,
        check_gitignore,
        check_render_config
    ]
    
    all_passed = True
    for check in checks:
        if not check():
            all_passed = False
        print()
    
    print("=" * 60)
    if all_passed:
        print("🎉 Toutes les vérifications sont passées !")
        print("✅ Votre projet est prêt pour le déploiement sur Render")
        print("\n📋 Prochaines étapes:")
        print("1. Initialisez git: git init")
        print("2. Ajoutez vos fichiers: git add .")
        print("3. Committez: git commit -m 'Initial commit'")
        print("4. Créez un dépôt GitHub")
        print("5. Poussez votre code: git push origin main")
        print("6. Suivez le guide DEPLOYMENT_RENDER.md")
    else:
        print("❌ Certaines vérifications ont échoué")
        print("🔧 Corrigez les problèmes avant de déployer")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 