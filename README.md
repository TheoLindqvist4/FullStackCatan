# 🎲 Jeu Catan en ligne avec FastAPI

### 📋 Description
Ce projet est une application web basée sur le jeu Catan, construite avec FastAPI. Il propose une plateforme en ligne permettant aux joueurs de s'inscrire, de se connecter, et de jouer au célèbre jeu de société Catan.

Le projet utilise une authentification basée sur les utilisateurs SQL plutôt qu’un système JWT. Les utilisateurs sont authentifiés via une gestion des sessions et des requêtes directes à la base de données.

Lors de la création d’un nouvel utilisateur, ses informations sont disponibles dans la section /profile, qui affiche également une photo de profil assignée aléatoirement à partir d’une sélection prédéfinie. Tant que vous ne redémarrez pas la base de données avec une commande docker compose down, vous pouvez créer plusieurs comptes. 

---

## 📂 Fonctionnalités principales

- **Inscription** : Les joueurs peuvent créer un compte avec un prénom, un nom, un email et un mot de passe.
- **Connexion** : Les joueurs peuvent se connecter en utilisant leur email et mot de passe.
- **Authentification SQL** : Basée sur les sessions et les requêtes à la base de données (pas de JWT).
- **Photos de profil aléatoires** : Chaque nouvel utilisateur se voit attribuer une image parmi un ensemble d'images prédéfinies.
- **Jeu en ligne** : Interface utilisateur inspirée du jeu de société Catan.

---

## 📦 Installation

### Prérequis

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/) et [Docker Compose](https://docs.docker.com/compose/)

### Étapes d'installation

1. **Clonez ce dépôt :**
   ```bash
   git clone https://TheoLindqvist4/FullStackCatan

2. **Installez les dépendances localement (optionnel, si vous ne voulez pas utiliser Docker) :**
   ```bash
   pip install -r requirements.txt

3. **Lancer l'application avec Docker Compose :**
   ```bash
   docker compose up --build

  ---

## 🔑 Routes principales

### 1. **Routes publiques**
- `GET /` : Page d'accueil.
- `GET /signup` : Page d'inscription.
- `POST /signup` : Crée un nouvel utilisateur.
- `GET /login` : Page de connexion.
- `POST /login` : Authentifie l'utilisateur.

### 2. **Routes protégées**
- `GET /profile` : Accessible uniquement aux joueurs connectés.
- `GET /play` : Interface de jeu inspirée de Catan.
- `GET /users` : Retourne une liste de tous les utilisateurs dans la base de données.

---
## 🖼️ Gestion des photos de profil

Lorsqu'un utilisateur s'inscrit, une photo de profil est choisie aléatoirement à partir du dossier static/images/profile_pictures. L’image attribuée est stockée dans la base de données avec les autres informations de l’utilisateur et est affichée sur la page /profile.

Remarque : Tant que la base de données n'est pas supprimée avec une commande docker compose down, toutes les informations et photos de profil des utilisateurs seront préservées.

## 🛠️ Configuration

### Structure du projet

Voici la structure principale du projet pour une meilleure compréhension :

```bash
projet
├── .env                   # Fichier des variables d'environnement (ex. : clés secrètes, configuration DB)
├── docker-compose.yml     # Configuration pour Docker Compose
├── Dockerfile             # Instructions pour construire l'image Docker
├── requirements.txt       # Liste des dépendances Python
│
└── app
    ├── main.py            # Point d'entrée de l'application (définit les routes principales)
    ├── __init__.py        # Fichier d'initialisation du module
    │
    ├── dependencies       # Gestion des dépendances et middlewares
    │
    ├── models             # Modèles de données pour la base de données (ex. : utilisateurs, profils)
    │
    ├── schemas            # Définition des schémas de données (ex. : validation des requêtes/réponses)
    │
    ├── services           # Logique métier (ex. : gestion des utilisateurs, services de jeu)
    │
    ├── static             # Fichiers statiques pour le frontend
    │   ├── style.css      # Fichier CSS principal
    │   └── images         # Images utilisées dans le projet (profils, ressources, etc.)
    │
    ├── templates          # Templates HTML pour l'interface utilisateur
    │   ├── base.html      # Template de base pour les autres pages
    │   ├── home.html      # Page d'accueil
    │   ├── login.html     # Page de connexion
    │   ├── play.html      # Interface du jeu
    │   ├── profile.html   # Page de profil utilisateur
    │   └── signup.html    # Page d'inscription
    │
    └── __pycache__        # Fichiers compilés Python (générés automatiquement)

```
### Explication des sections principales :

- **Game.py** : Contient la logique principale du jeu.
- **README.md** : Documentation détaillée pour comprendre et exécuter le projet.
- **Application_Full_Stack/projet** : Répertoire contenant l'application complète.
  - **.env** : Contient les variables d'environnement sensibles (ex. : mots de passe, clés API).
  - **app/** : Structure principale de l'application avec :
    - **models/** : Définitions des modèles pour la base de données.
    - **templates/** : Fichiers HTML pour l'interface utilisateur.

---

## 🧪 Tests

### Étapes pour tester :

1. **Inscription :**
   - Accédez à `/signup`.
   - Créez un compte avec un email et un mot de passe valides.

2. **Connexion :**
   - Accédez à `/login` avec vos identifiants.
   - Vérifiez que vous êtes redirigé vers `/profile` après connexion.
   - Vérifiez que chaque nouvel utilisateur se voit attribuer une photo de profil différente (aléatoire).

3. **Route protégé :**
   - Essayez d'accéder à `/profile` sans être connecté. Vous devriez recevoir une erreur `401 Unauthorized`.
   - Connectez-vous, puis accédez à la page protégé.

---

## 📖 Technologies utilisées

- **Framework Backend** : [FastAPI](https://fastapi.tiangolo.com/)
- **Base de données** : PostgreSQL
- **Frontend** : HTML, CSS, Jinja2 Templates
- **Infrastructure** : Docker & Docker Compose
- **Gestion des mots de passe** : passlib[bcrypt]
