# Architecture — Analyse Uber

## Flux

```
generate.py → CSV brut
     │
     ▼
extract.py → transform.py (vitesse, nettoyage)
     │
     ▼
  load.py → uber.db
     │
     ├── Indicateurs (console)
     └── visualize.py
              │
              ▼
         charts/
         ├── trajets_par_zone.png
         ├── prix_moyen_par_zone.png
         └── distance_vs_prix.png
```

## Table `trajets`

- date, zone_depart, zone_arrivee
- distance_km, duree_min, prix
- vitesse_kmh

## Visualisations

| Fichier | Contenu |
|---------|---------|
| trajets_par_zone.png | Barres : volume par zone de départ |
| prix_moyen_par_zone.png | Barres horizontales : prix moyen |
| distance_vs_prix.png | Nuage de points distance vs prix |
