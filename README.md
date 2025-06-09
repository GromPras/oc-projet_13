## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

### Prérequis

- Un compte Render
- Un compte DockerHub avec un répertoire public

### Description

Le répertoire du projet intègre :
- L'automatisation des tests aux push sur chaque branche
- Un build de l'image docker aux push sur toutes les branches également
- Le déploiement de l'application, après validation manuelle par une personne autorisée, si push sur la branche `main`

### Configuration

Afin de mettre en place le déploiement automatique il faut paramétrer certaines variables d'environement

#### Côté GitHub
Créer les Secrets suivants dans settings>Secrets and variables :
- `DOCKERHUB_TOKEN` & `DOCKERHUB_TOKEN` pour la mise en ligne de l'image sur DockerHub
- `SENTRY_DSN` pour permettre le build de l'application et de l'image
- `WEBHOOK_URL` pour le déploiement sur Render

Dans l'environnement `deploy-approval`, assurez-vous que vous ou votre équipe faites partie da la liste des reviewers autorisés à approuver le déploiement.


#### Côté Render
Dans l'environnement du projet, créer les variables suivantes :
- `SENTRY_DSN` pour, cette fois, permettre la surveillance des erreurs en temps réel
- `ALLOWED_HOSTS` afin que l'application tourne sur le serveur de déploiement

### Déployer l'application

Pour éffectuer le déploiement, une fois que les variables d'environement sont déclarées sur les différentes plateformes :

- Après avoir fait vos modifications, faites un push sur la branche `main`
- La phase de test se lance et soulève une erreur si la couverture des tests est inférieure à 80% ou si l'application ne peut pas être compilée
- Si l'étape précédente est passée avec succés l'image Docker est compilée est mise en ligne sur le répertoire DockerHub
- GitHub met la pipeline en pause en attendant la confirmation du déploiement si les deux étapes ont réussi
- Une fois le déploiement confirmé par vous ou une autre personne autorisée, le déploiement est déclanché sur Render
- Render va alors chercher l'image qui correspond au dernier commit et lance le serveur
