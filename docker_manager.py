import docker 

def list_containers():
    # Connexion à Docker
    client = docker.from_env()
    
    # Récupération des conteneurs
    containers = client.containers.list(all=True)
    
    # Affichage
    for container in containers:
        print(f"ID: {container.id[:12]}")
        print(f"Nom: {container.name}")
        print(f"Status: {container.status}")
        print("-" * 20)

# Appel de la fonction
if __name__ == "__main__":
    list_containers()