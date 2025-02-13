# Projet : Monitoring d'API avec Python et DevOps



Solution complète de monitoring d'API implémentant des bonnes pratiques DevOps avec :
- Vérification de statut d'API
- Logging centralisé
- Containerisation Docker
- CI/CD automatisée

## Fonctionnalités Clés
- ✅ Monitoring temps réel d'API
- 📝 Logging structuré dans `api_monitor.log`
- 🐳 Build et déploiement Docker automatisé
- 🔄 CI/CD avec GitHub Actions
- 🧪 Tests unitaires avec pytest

## Execution

#### Mode natif
```bash
python monitor.py
```

#### Avec Docker
```bash
docker-compose up --build
```

#### Mode production

```bash
docker run -e API_URL=<your-api-url> <username>/api-monitor
```

### Fonctions clés

| Fonction | Description | Technologies Utilisées |
|----------|-------------|----------------------|
| `_setup_logging()` | Configure le système de logging | logging, os |
| `check_status()` | Vérifie le statut de l'API | requests, exception handling |
| `monitor()` | Point d'entrée principal du monitoring | logging, print |


### Évolution Possible
- 🔊 Intégration avec Prometheus/Grafana
- 📨 Notifications Slack/Email
- 🌐 Déploiement Kubernetes
- 🔍 Analyse de logs avec ELK Stack