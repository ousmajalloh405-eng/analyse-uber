"""Transformation des trajets Uber."""

from typing import List, Dict


def transformer(lignes: List[Dict]) -> List[Dict]:
    propres = []
    for ligne in lignes:
        try:
            distance = float(ligne["distance_km"])
            duree = int(ligne["duree_min"])
            prix = float(ligne["prix"])
            if distance <= 0 or duree <= 0 or prix <= 0:
                continue
            vitesse = round(distance / (duree / 60), 1)
            propres.append({
                "date": ligne["date"],
                "zone_depart": ligne["zone_depart"].strip(),
                "zone_arrivee": ligne["zone_arrivee"].strip(),
                "distance_km": distance,
                "duree_min": duree,
                "prix": prix,
                "vitesse_kmh": vitesse,
            })
        except (ValueError, KeyError):
            continue
    return propres
