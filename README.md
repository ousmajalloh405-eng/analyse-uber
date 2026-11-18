# Analyse des données Uber

> Pipeline ETL d’analyse de trajets Uber (génération, nettoyage, indicateurs + **visualisation**).

**Statut** : 🟢 Réalisé  
**Catégorie** : ⚙️ Création de pipelines ETL  
**Portfolio** : [Profil GitHub](https://github.com/ousmajalloh405-eng)

---

## 1. Problème métier

Analyser les trajets Uber pour comprendre les distances, durées, prix et zones les plus demandées, puis **visualiser** les résultats.

## 2. Architecture

```
generate.py → trajets_bruts.csv
      │
      ▼
 extract.py → transform.py → load.py → uber.db
                                      │
                                      ├── Indicateurs (console)
                                      └── visualize.py → charts/*.png
```

## 3. Technologies

- Python 3
- Bibliothèque standard
- SQLite
- **matplotlib** (graphiques)

## 4. Installation et exécution

```bash
git clone https://github.com/ousmajalloh405-eng/analyse-uber.git
cd analyse-uber
python3 -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 main.py
```

Les graphiques sont générés dans le dossier `charts/` :
- `trajets_par_zone.png` — nombre de trajets par zone
- `prix_moyen_par_zone.png` — prix moyen par zone
- `distance_vs_prix.png` — relation distance / prix

## 5. Indicateurs produits

- Prix moyen, distance moyenne, durée moyenne
- Top zones de départ
- Trajets les plus chers
- Graphiques PNG

## 6. Compétences pour le CV

Développement d’un pipeline ETL pour l’analyse de données de mobilité (trajets Uber), avec calcul d’indicateurs métier et visualisation matplotlib.

---

*Projet réalisé dans le cadre de la formation Data — Sonatel Academy.*
