"""Pipeline d'analyse des trajets Uber."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from generate import generer_trajets
from extract import extraire
from transform import transformer
from load import initialiser_base, charger


CSV_PATH = Path(__file__).parent / "data" / "trajets_bruts.csv"
DB_PATH = Path(__file__).parent / "data" / "uber.db"


def afficher_indicateurs(conn):
    print("\n=== Indicateurs Uber ===")

    row = conn.execute("""
        SELECT ROUND(AVG(prix), 0), ROUND(AVG(distance_km), 1), ROUND(AVG(duree_min), 0)
        FROM trajets
    """).fetchone()
    print(f"Prix moyen : {row[0]} FCFA")
    print(f"Distance moyenne : {row[1]} km")
    print(f"Durée moyenne : {row[2]} min")

    print("\nTop zones de départ :")
    for r in conn.execute("""
        SELECT zone_depart, COUNT(*) AS nb
        FROM trajets
        GROUP BY zone_depart
        ORDER BY nb DESC
        LIMIT 5
    """):
        print(f"  {r[0]:15} {r[1]} trajets")

    print("\n3 trajets les plus chers :")
    for r in conn.execute("""
        SELECT zone_depart, zone_arrivee, prix, distance_km
        FROM trajets
        ORDER BY prix DESC
        LIMIT 3
    """):
        print(f"  {r[0]} → {r[1]} : {r[2]} FCFA ({r[3]} km)")


def main():
    print("=== Analyse trajets Uber ===\n")

    generer_trajets(500, CSV_PATH)

    brut = extraire(CSV_PATH)
    print(f"Trajets extraits : {len(brut)}")

    propres = transformer(brut)
    print(f"Après nettoyage : {len(propres)}")

    conn = initialiser_base(DB_PATH)
    nb = charger(conn, propres)
    print(f"Chargés dans {DB_PATH} : {nb}")

    afficher_indicateurs(conn)
    conn.close()
    print("\nPipeline terminé.")


if __name__ == "__main__":
    main()
