# Analyse des données Uber

> Pipeline ETL d’analyse de trajets Uber (génération, nettoyage, indicateurs).

**Statut** : 🟢 Réalisé
**Catégorie** : ⚙️ Création de pipelines ETL
**Portfolio** : [Profil GitHub](https://github.com/ousmajalloh405-eng)

---

## 1. Problème métier

Analyser les trajets Uber pour comprendre les distances, durées, prix et zones les plus demandées.

## 2. Architecture

```
generate.py → trajets_bruts.csv
      │
      ▼
 extract.py → transform.py → load.py → uber.db
                                      │
                                      ▼
                               Indicateurs (prix, zones, distance)
```

## 3. Technologies

- Python 3
- Bibliothèque standard
- SQLite

## 4. Installation et exécution

```bash
git clone https://github.com/ousmajalloh405-eng/analyse-uber.git
cd analyse-uber
python3 main.py
```

## 5. Indicateurs produits

- Prix moyen, distance moyenne, durée moyenne
- Top zones de départ
- Trajets les plus chers

## 6. Compétences pour le CV

Développement d’un pipeline ETL pour l’analyse de données de mobilité (trajets Uber), avec calcul d’indicateurs métier.

---

*Projet réalisé dans le cadre de la formation Data — Sonatel Academy.*
