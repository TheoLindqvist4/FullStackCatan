# 🎲 Jeu Catan en ligne avec FastAPI

### 📋 Description
Ce projet est une application web basée sur le jeu **Catan**, construite avec **FastAPI**. Il propose une plateforme en ligne permettant aux joueurs de s'inscrire, de se connecter, et de jouer au célèbre jeu de société Catan. Le projet utilise un système d'authentification sécurisé basé sur **JWT (JSON Web Tokens)** pour protéger les fonctionnalités accessibles uniquement aux utilisateurs connectés.

---

## 📂 Fonctionnalités principales

- **Inscription** : Les joueurs peuvent créer un compte.
- **Connexion** : Les joueurs peuvent se connecter en utilisant leur email et mot de passe.
- **Authentification JWT** : Utilisation des tokens pour sécuriser les routes protégées.
- **Jeu en ligne** : Interface utilisateur inspirée du jeu de société Catan.
- **Gestion sécurisée des mots de passe** : Hachage des mots de passe avec `bcrypt`.
- **Cookies sécurisés** : Stockage du token JWT dans des cookies protégés.
- **Surveillance des performances** : Intégration de `PrometheusMiddleware` pour surveiller l'application.

---

## 📦 Installation

### Prérequis

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/) et [Docker Compose](https://docs.docker.com/compose/)

### Étapes d'installation

1. **Clonez ce dépôt :**
   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-repo.git

2. **Créez et configurez votre fichier `.env` :**
   Créez un fichier `.env` à la racine du projet et ajoutez-y les variables d'environnement suivantes :
   ```env
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=your_database
   SECRET_KEY=your_secret_key

3. **Installez les dépendances localement (optionnel, si vous ne voulez pas utiliser Docker) :**
   ```bash
   pip install -r requirements.txt

4. **Lancer l'application avec Docker Compose :**
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

---

## 🛠️ Configuration

### Structure du projet

Voici la structure principale du projet pour une meilleure compréhension :

```bash
FullStackCatan
├── Game.py                # Script principal du jeu
├── README.md              # Documentation du projet
├── test.py                # Script pour les tests
├── .git/                  # Dossier pour la gestion Git
├── Application_Full_Stack
│   └── projet
│       ├── .env               # Fichier des variables d'environnement
│       ├── docker-compose.yml # Configuration Docker Compose
│       ├── Dockerfile         # Configuration Docker
│       ├── requirements.txt   # Liste des dépendances Python
│       └── app
│           ├── main.py        # Point d'entrée de l'application
│           ├── __init__.py    # Fichier d'initialisation
│           ├── dependencies   # Gestion des dépendances
│           ├── images         # Images utilisées dans le jeu
│           ├── models         # Gestion des modèles (Base de données)
│           ├── routers        # Gestion des routes API
│           ├── schemas        # Schémas des données
│           ├── services       # Services et logique métier
│           ├── static         # Fichiers CSS et JS
│           ├── templates      # Fichiers HTML (Jinja2)
│           └── __pycache__    # Fichiers compilés Python
```
### Explication des sections principales :

- **Game.py** : Contient la logique principale du jeu.
- **README.md** : Documentation détaillée pour comprendre et exécuter le projet.
- **Application_Full_Stack/projet** : Répertoire contenant l'application complète.
  - **.env** : Contient les variables d'environnement sensibles (ex. : mots de passe, clés API).
  - **app/** : Structure principale de l'application avec :
    - **models/** : Définitions des modèles pour la base de données.
    - **routers/** : Routes API pour les fonctionnalités de l'application.
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

3. **Routes protégées :**
   - Essayez d'accéder à `/profile` ou `/play` sans être connecté. Vous devriez recevoir une erreur `401 Unauthorized`.
   - Connectez-vous, puis accédez aux pages protégées.

4. **Vérification des cookies :**
   - Assurez-vous que le token JWT est stocké dans un cookie après connexion.

---

## 📖 Technologies utilisées

- **Framework Backend** : [FastAPI](https://fastapi.tiangolo.com/)
- **Base de données** : PostgreSQL
- **Authentification** : JSON Web Tokens (JWT) avec `jose`
- **Hachage des mots de passe** : `passlib[bcrypt]`
- **Frontend** : HTML, CSS, Jinja2 Templates
- **Infrastructure** : Docker & Docker Compose
- **Surveillance** : `PrometheusMiddleware`
