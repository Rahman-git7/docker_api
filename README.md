# Python Docker Manager

## Concepts de Base

### Import et Configuration
```python
import docker
client = docker.from_env()  # Connexion à l'environnement Docker
```

### Structure d'une Fonction
```python
def list_images():
    # Code
    pass

if __name__ == "__main__":  # Point d'entrée du programme
    list_images()
```

### Boucles et Conditions
```python
# Boucle for pour parcourir une liste
for image in images:
    if condition:  # Test conditionnel
        # Action
```

## Conventions de Nommage
- Utiliser le singulier pour un élément : `image`
- Utiliser le pluriel pour les listes : `images`
- Exemple : `for image in images`

## Bonnes Pratiques
- Vérifier l'existence des données avant utilisation
- Utiliser des noms de variables explicites
- Commenter le code pour expliquer sa logique

## Syntaxe Importante
- f-strings : `f"ID: {image.id}"`
- Vérification des conditions : `if image.tags and condition`
- Point d'entrée : `if __name__ == "__main__"`

# Projet : Monitoring d'une API en Python

Script Python pour surveiller le statut d'une API. Le script vérifie si l'API est en ligne, charge l'URL depuis un fichier de configuration, et enregistre les résultats dans un fichier log.

---

## Fonctionnalités
1. Vérifie le statut d'une API via une requête HTTP.
2. Charge l'URL de l'API depuis un fichier de configuration (`config.ini`).
3. Enregistre les résultats dans un fichier log (`api_monitor.log`).

---

## Étapes et Concepts

### 1. Vérifier le statut de l'API
- **Bibliothèque `requests`** : Envoie une requête GET à l'API et vérifie le code de statut.
  - `requests.get(url)` : Envoie la requête.
  - `response.status_code` : Retourne le code HTTP (200 = en ligne).
- **Gestion des erreurs** : Capture les erreurs de connexion avec `try-except`.

```python
import requests

def check_api_status(url):
    try:
        response = requests.get(url)
        return "online" if response.status_code == 200 else f"offline: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"error: {e}"
```

### 2.  Charger l'URL depuis un fichier de configuration

Module configparser : Lit un fichier `.ini` pour charger l'URL de l'API.

* `config.read('config.ini')` : Lit le fichier.
* `config['api']['url']` : Récupère l'URL.

### 3. Enregistrer les résultats dans un fichier log

Module logging : Enregistre les statuts dans un fichier log.
* `logging.basicConfig()` : Configure le fichier log.
* `logging.info(message)` : Enregistre un message.

