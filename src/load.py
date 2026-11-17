"""Chargement des trajets dans SQLite."""

import sqlite3
from pathlib import Path
from typing import List, Dict


def initialiser_base(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS trajets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            zone_depart TEXT,
            zone_arrivee TEXT,
            distance_km REAL,
            duree_min INTEGER,
            prix REAL,
            vitesse_kmh REAL
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_zone_depart ON trajets(zone_depart)")
    conn.commit()
    return conn


def charger(conn: sqlite3.Connection, data: List[Dict]) -> int:
    conn.execute("DELETE FROM trajets")
    for t in data:
        conn.execute(
            """INSERT INTO trajets 
               (date, zone_depart, zone_arrivee, distance_km, duree_min, prix, vitesse_kmh)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (t["date"], t["zone_depart"], t["zone_arrivee"],
             t["distance_km"], t["duree_min"], t["prix"], t["vitesse_kmh"]),
        )
    conn.commit()
    return len(data)
