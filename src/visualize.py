"""Visualisation des trajets Uber (graphiques matplotlib)."""

from pathlib import Path
import sqlite3


def generer_graphiques(conn: sqlite3.Connection, output_dir: Path) -> list:
    """Génère 3 graphiques à partir de la base et les enregistre en PNG."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib non installé. Exécutez: pip install matplotlib")
        return []

    output_dir.mkdir(parents=True, exist_ok=True)
    fichiers = []

    rows = conn.execute("""
        SELECT zone_depart, COUNT(*) AS nb
        FROM trajets
        GROUP BY zone_depart
        ORDER BY nb DESC
    """).fetchall()
    if rows:
        zones = [r[0] for r in rows]
        counts = [r[1] for r in rows]
        fig, ax = plt.subplots(figsize=(9, 5))
        bars = ax.bar(zones, counts, color="#1f77b4", edgecolor="white")
        ax.set_title("Nombre de trajets par zone de départ", fontsize=14, fontweight="bold")
        ax.set_xlabel("Zone")
        ax.set_ylabel("Nombre de trajets")
        ax.tick_params(axis="x", rotation=30)
        for bar, c in zip(bars, counts):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                    str(c), ha="center", va="bottom", fontsize=9)
        fig.tight_layout()
        path = output_dir / "trajets_par_zone.png"
        fig.savefig(path, dpi=120)
        plt.close(fig)
        fichiers.append(path)
        print(f"  Graphique : {path.name}")

    rows = conn.execute("""
        SELECT zone_depart, ROUND(AVG(prix), 0) AS prix_moyen
        FROM trajets
        GROUP BY zone_depart
        ORDER BY prix_moyen DESC
    """).fetchall()
    if rows:
        zones = [r[0] for r in rows]
        prix = [r[1] for r in rows]
        fig, ax = plt.subplots(figsize=(9, 5))
        bars = ax.barh(zones, prix, color="#2ca02c", edgecolor="white")
        ax.set_title("Prix moyen par zone de départ (FCFA)", fontsize=14, fontweight="bold")
        ax.set_xlabel("Prix moyen (FCFA)")
        ax.set_ylabel("Zone")
        for bar, p in zip(bars, prix):
            ax.text(bar.get_width() + 50, bar.get_y() + bar.get_height() / 2,
                    f"{int(p)}", va="center", fontsize=9)
        fig.tight_layout()
        path = output_dir / "prix_moyen_par_zone.png"
        fig.savefig(path, dpi=120)
        plt.close(fig)
        fichiers.append(path)
        print(f"  Graphique : {path.name}")

    rows = conn.execute("""
        SELECT distance_km, prix FROM trajets LIMIT 300
    """).fetchall()
    if rows:
        distances = [r[0] for r in rows]
        prix_list = [r[1] for r in rows]
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(distances, prix_list, alpha=0.5, c="#ff7f0e", s=25, edgecolors="none")
        ax.set_title("Relation distance (km) / prix (FCFA)", fontsize=14, fontweight="bold")
        ax.set_xlabel("Distance (km)")
        ax.set_ylabel("Prix (FCFA)")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        path = output_dir / "distance_vs_prix.png"
        fig.savefig(path, dpi=120)
        plt.close(fig)
        fichiers.append(path)
        print(f"  Graphique : {path.name}")

    return fichiers
