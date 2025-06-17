# 🎶 Musipedia

Un dictionnaire collaboratif des genres musicaux, construit en JSON et versionné avec GitHub.

## 📁 Structure
- `/genres/` : chaque fichier est un genre musical (`.json`)
- `/scripts/` : scripts Python (`viewer`, `search`, `merge`)
- `catalogue.json` : fusion de tous les genres
- GitHub Action : valide les JSON et génère le catalogue

## 🔧 Commandes utiles
```bash
# Voir un genre
python scripts/viewer.py synthwave

# Chercher un mot-clé
python scripts/search.py kavinsky

# Fusionner tous les fichiers
python scripts/merge.py
```