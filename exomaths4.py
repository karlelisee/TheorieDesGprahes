"""
TP Graphe – Exercice 4
"""

import math

def floyd_warshall(matrice):
    """
    Implémente l'algorithme de Floyd-Warshall.
    :param matrice: matrice carrée des poids (math.inf pour absence d’arête)
    :return: matrice des plus courts chemins + prédécesseurs
    """
    n = len(matrice)
    dist = [[matrice[i][j] for j in range(n)] for i in range(n)]
    pred = [[None if (i == j or matrice[i][j] == math.inf) else i for j in range(n)] for i in range(n)]

    print("=== ALGORITHME DE FLOYD-WARSHALL ===\n")
    for k in range(n):
        print(f"--- Itération k = {k + 1} ---")
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
        for ligne in dist:
            print(["∞" if x == math.inf else x for x in ligne])
        print()
    return dist, pred


def reconstituer_chemin(pred, i, j):
    """Reconstitue le chemin de i à j à partir des prédécesseurs."""
    if pred[i][j] is None:
        return None
    chemin = [j]
    while j != i:
        j = pred[i][j]
        chemin.insert(0, j)
    return chemin



# TEST SUR UN GRAPHE (TD Chemins Optimaux 2)

if __name__ == "__main__":
    print("\n==================== FLOYD-WARSHALL ====================\n")

    # Matrice des poids : A, B, C, D, E
    # ∞ = pas d’arête directe
    M = [
        [0,  math.inf, 3, 2, math.inf],   # A
        [math.inf, 0, math.inf, -2, 5],   # B
        [math.inf, 2, 0, -1, math.inf],   # C
        [math.inf, math.inf, 2, 0, 3],    # D
        [math.inf, math.inf, math.inf, math.inf, 0]  # E
    ]

    dist, pred = floyd_warshall(M)

    print("=== MATRICE FINALE DES PLUS COURTS CHEMINS ===")
    for ligne in dist:
        print(["∞" if x == math.inf else x for x in ligne])

    # Exemple de reconstitution de chemin
    i, j = 0, 4  # de A à E
    chemin = reconstituer_chemin(pred, i, j)
    if chemin:
        noms = ['A', 'B', 'C', 'D', 'E']
        print(f"\nPlus court chemin de {noms[i]} à {noms[j]} :", " → ".join(noms[x] for x in chemin))
        print(f"Distance totale : {dist[i][j]}")
    else:
        print(f"\nAucun chemin de {noms[i]} à {noms[j]}.")
