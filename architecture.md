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
     ▼
Indicateurs
```

## Table `trajets`

- date, zone_depart, zone_arrivee
- distance_km, duree_min, prix
- vitesse_kmh
