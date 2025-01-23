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