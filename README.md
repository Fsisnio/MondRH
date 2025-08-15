# 🌟 MonDRH - Plateforme de Ressources Humaines

Une plateforme moderne et professionnelle pour la gestion des ressources humaines, incluant recrutement, coaching, formation, intérim et conseil.

## ✨ Fonctionnalités

### 🎯 Fonctionnalités principales
- **Gestion des candidatures** : Soumission et suivi des candidatures
- **Rendez-vous** : Prise de rendez-vous et gestion du calendrier
- **Dashboard professionnel** : Interface moderne avec statistiques
- **Administration** : Panel d'administration complet
- **Intégration Google Workspace** : Drive et Calendar

### 🔗 Intégrations
- **Google Drive** : Sauvegarde automatique des CV
- **Google Calendar** : Synchronisation des rendez-vous
- **Email** : Notifications automatiques

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip
- Compte Google Cloud (pour l'intégration Google Workspace)

### Installation rapide

1. **Cloner le projet**
```bash
git clone <repository-url>
cd monderh
```

2. **Créer l'environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer Google OAuth (optionnel mais recommandé)**
```bash
# Suivre le guide complet
python setup_google_oauth.py
```

5. **Créer l'administrateur**
```bash
python create_admin_auto.py
```

6. **Lancer l'application**
```bash
python app.py
```

L'application sera accessible sur `http://localhost:5001`

## 🔧 Configuration Google Workspace

### Configuration automatique
```bash
python setup_google_oauth.py
```

### Configuration manuelle
1. Suivez le guide : `GOOGLE_SETUP_GUIDE.md`
2. Créez un fichier `.env` basé sur `env.example`
3. Ajoutez vos clés Google OAuth

### Vérification de la configuration
```bash
python check_google_config.py
```

## 👤 Comptes par défaut

### Administrateur
- **Email** : `admin@monderh.fr`
- **Mot de passe** : `admin123`

## 📁 Structure du projet

```
monderh/
├── app.py                      # Application principale
├── requirements.txt            # Dépendances Python
├── .env                        # Variables d'environnement (à créer)
├── env.example                 # Exemple de configuration
├── static/                     # Fichiers statiques
│   ├── css/
│   │   ├── style.css          # Styles globaux
│   │   └── dashboard.css      # Styles du dashboard
│   ├── js/
│   └── uploads/               # Fichiers uploadés
├── templates/                  # Templates HTML
│   ├── admin/                 # Templates d'administration
│   ├── auth/                  # Templates d'authentification
│   ├── dashboard/             # Templates du dashboard
│   └── base.html              # Template de base
├── instance/                  # Base de données SQLite
├── scripts/                   # Scripts utilitaires
│   ├── check_google_config.py # Vérification Google OAuth
│   ├── setup_google_oauth.py  # Configuration Google OAuth
│   └── create_admin_auto.py   # Création admin automatique
└── docs/                      # Documentation
    ├── GOOGLE_SETUP_GUIDE.md  # Guide Google OAuth
    └── DASHBOARD_IMPROVEMENTS.md # Améliorations dashboard
```

## 🎨 Interface utilisateur

### Dashboard moderne
- Design professionnel avec gradients
- Cartes de statistiques interactives
- Intégration Google Workspace
- Interface responsive

### Administration
- Panel d'administration complet
- Gestion des utilisateurs
- Configuration du site
- Suivi des candidatures et rendez-vous

## 🔒 Sécurité

- Authentification sécurisée
- Hachage des mots de passe
- Protection CSRF
- Variables d'environnement pour les secrets
- Validation des formulaires

## 🛠️ Développement

### Variables d'environnement
```env
# Google OAuth (requis pour Google Workspace)
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret

# Email (optionnel)
MAIL_USERNAME=contact@monderh.fr
MAIL_PASSWORD=your-email-password

# Flask
SECRET_KEY=your-secret-key
```

### Base de données
- SQLite par défaut (développement)
- Support PostgreSQL/MySQL (production)

## 📱 Fonctionnalités avancées

### Intégration Google Workspace
- **Google Drive** : Sauvegarde automatique des CV
- **Google Calendar** : Synchronisation des rendez-vous
- **OAuth 2.0** : Authentification sécurisée

### Dashboard professionnel
- **Statistiques en temps réel**
- **Graphiques interactifs**
- **Notifications**
- **Actions rapides**

## 🚀 Déploiement

### Production
1. Configurer les variables d'environnement
2. Utiliser un serveur WSGI (Gunicorn, uWSGI)
3. Configurer un reverse proxy (Nginx)
4. Utiliser HTTPS
5. Configurer la base de données de production

### Docker (à venir)
```bash
docker build -t monderh .
docker run -p 5000:5000 monderh
```

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature
3. Commiter les changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📞 Support

- **Documentation** : Consultez les guides dans le dossier `docs/`
- **Issues** : Utilisez les issues GitHub
- **Email** : contact@monderh.fr

---

*Développé avec ❤️ pour simplifier la gestion RH* 