"""
TP Graphe Exercice 2 : Fermeture transitive (Algorithme de Roy-Warshall)
"""

def roy_warshall(matrice):
    """
    Implémente l’algorithme de Roy-Warshall pour la fermeture transitive.
    :param matrice: matrice d’adjacence (liste de listes)
    :return: matrice de la fermeture transitive
    """
    n = len(matrice)
    fermeture = [ligne[:] for ligne in matrice]  # copie de la matrice initiale

    print("=== Algorithme de Roy-Warshall ===\n")
    for k in range(n):
        print(f"--- Itération k = {k + 1} ---")
        for i in range(n):
            for j in range(n):
                if fermeture[i][j] == 0 and (fermeture[i][k] and fermeture[k][j]):
                    fermeture[i][j] = 1
        # Affichage intermédiaire
        for ligne in fermeture:
            print(ligne)
        print()
    return fermeture


# Exemple de test : Graphe G1
G1 = [
    [0, 1, 1, 1, 0],  # C1
    [0, 0, 0, 0, 1],  # C2
    [0, 0, 0, 1, 0],  # C3
    [0, 0, 0, 0, 1],  # C4
    [0, 0, 0, 0, 0]   # C5
]

# Graphe G2
G2 = [
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

# Graphe de l’exercice 7 du TD Graphe_1


G3 = [
    [0, 1, 1],  # C1
    [0, 0, 1],  # C2
    [0, 0, 0]   # C3
]
# TESTS DES TROIS GRAPHES
if __name__ == "__main__":
    print("\n==================== FERMETURE TRANSITIVE G1 ====================\n")
    fermeture_G1 = roy_warshall(G1)
    print("Fermeture transitive G1 :")
    for ligne in fermeture_G1:
        print(ligne)

    print("\n==================== FERMETURE TRANSITIVE G2 ====================\n")
    fermeture_G2 = roy_warshall(G2)
    print("Fermeture transitive G2 :")
    for ligne in fermeture_G2:
        print(ligne)

    print("\n==================== FERMETURE TRANSITIVE G3 (Ex.7 TD) ====================\n")
    fermeture_G3 = roy_warshall(G3)
    print("Fermeture transitive G3 :")
    for ligne in fermeture_G3:
        print(ligne)

    # Vérification si G1 et G2 sont τ-équivalents
    print("\n==================== COMPARAISON G1 / G2 ====================\n")
    if fermeture_G1 == fermeture_G2:
        print(" G1 et G2 sont τ-équivalents (même fermeture transitive).")
    else:
        print(" G1 et G2 ne sont PAS τ-équivalents.")

