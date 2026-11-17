"""Génération de données fictives de trajets Uber."""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

ZONES = ["Plateau", "Almadies", "Parcelles", "Ouakam", "Mermoz", "Ngor", "Yoff"]


def generer_trajets(n: int = 500, fichier: Path = Path("data/trajets_bruts.csv")) -> None:
    fichier.parent.mkdir(parents=True, exist_ok=True)
    debut = datetime(2026, 10, 1)
    with open(fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "zone_depart", "zone_arrivee", "distance_km", "duree_min", "prix"])
        for _ in range(n):
            date = debut + timedelta(days=random.randint(0, 40), hours=random.randint(6, 22))
            depart = random.choice(ZONES)
            arrivee = random.choice([z for z in ZONES if z != depart])
            distance = round(random.uniform(1.5, 25), 1)
            duree = int(distance * random.uniform(2.5, 5))
            prix = round(distance * random.uniform(200, 450), 0)
            writer.writerow([
                date.strftime("%Y-%m-%d %H:%M"),
                depart,
                arrivee,
                distance,
                duree,
                prix,
            ])
    print(f"{n} trajets générés dans {fichier}")
