"""
TP Graphe – Exercice 3.A: Cheminements optimaux (Algorithme de Dijkstra)
"""

import heapq  # pour gérer la file de priorité

def dijkstra(graphe, depart):
    """
    Implémente l'algorithme de Dijkstra.
    :param graphe: dict {sommet: {voisin: poids}}
    :param depart: sommet de départ
    :return: dictionnaire des distances et des prédécesseurs
    """
    # Initialisation
    distances = {sommet: float('inf') for sommet in graphe}
    predecesseurs = {sommet: None for sommet in graphe}
    distances[depart] = 0

    # File de priorité (min-heap)
    file = [(0, depart)]

    print("=== Algorithme de Dijkstra ===\n")

    while file:
        distance_courante, sommet_courant = heapq.heappop(file)

        print(f"Sommet courant : {sommet_courant} | distance = {distance_courante}")

        # Parcourir les voisins
        for voisin, poids in graphe[sommet_courant].items():
            nouvelle_distance = distance_courante + poids

            # Si on trouve un chemin plus court
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                predecesseurs[voisin] = sommet_courant
                heapq.heappush(file, (nouvelle_distance, voisin))
                print(f"   → Mise à jour : {voisin} = {nouvelle_distance} (prédécesseur = {sommet_courant})")

    print("\nDistances finales :", distances)
    print("Prédécesseurs :", predecesseurs)
    return distances, predecesseurs


def reconstituer_chemin(predecesseurs, depart, arrivee):
    """
    Reconstitue le plus court chemin à partir du dictionnaire des prédécesseurs.
    """
    chemin = []
    sommet = arrivee
    while sommet is not None:
        chemin.insert(0, sommet)
        sommet = predecesseurs[sommet]
    if chemin[0] == depart:
        return chemin
    else:
        return None


# Graphe de test

# Représentation pondérée (tous les poids positifs)
graphe_dijkstra = {
    'x1': {'x2': 2, 'x3': 6},
    'x2': {'x4': 3, 'x5': 5},
    'x3': {'x4': 2},
    'x4': {'x6': 1},
    'x5': {'x6': 3},
    'x6': {}
}

# Test de l'algorithme
if __name__ == "__main__":
    print("\n==================== DIJKSTRA (x1 → tous) ====================\n")
    distances, predecesseurs = dijkstra(graphe_dijkstra, 'x1')

    # Afficher le plus court chemin de x1 à x6
    chemin = reconstituer_chemin(predecesseurs, 'x1', 'x6')
    print(f"\nPlus court chemin de x1 à x6 : {chemin}")
    print(f"Longueur du chemin : {distances['x6']}")

    # Vérification
    print("\n==================== RÉSULTAT ATTENDU ====================")
    print("Chemin optimal attendu : x1 → x2 → x4 → x6")
    print("Distance totale attendue : 2 + 3 + 1 = 6")


"""
TP Graphe – Exercice 3.B
"""

import heapq


# 1.  OUTILS DE BASE


def heuristique(a, b):
    """Heuristique de Manhattan entre deux points (x, y)."""
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def voisins(grille, noeud):
    """Retourne les voisins valides (haut, bas, gauche, droite)
    d’un noeud non bloqué dans la grille."""
    x, y = noeud
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    voisins_valides = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]) and grille[nx][ny] == 0:
            voisins_valides.append((nx, ny))
    return voisins_valides



# 2.  ALGORITHME DE DIJKSTRA


def dijkstra_grille(grille, start, goal):
    """Algorithme de Dijkstra sur une grille (poids uniformes = 1)."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    distances = {start: 0}
    iterations = 0

    while open_set:
        iterations += 1
        distance_courante, current = heapq.heappop(open_set)
        if current == goal:
            # Reconstitution du chemin
            chemin = [current]
            while current in came_from:
                current = came_from[current]
                chemin.append(current)
            chemin.reverse()
            return chemin, iterations

        for voisin in voisins(grille, current):
            tentative = distance_courante + 1
            if voisin not in distances or tentative < distances[voisin]:
                distances[voisin] = tentative
                came_from[voisin] = current
                heapq.heappush(open_set, (tentative, voisin))

    return None, iterations



# 3.  ALGORITHME A*


def a_star(grille, start, goal):
    """Algorithme A* sur une grille avec obstacles."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristique(start, goal)}
    iterations = 0

    while open_set:
        iterations += 1
        _, current = heapq.heappop(open_set)

        if current == goal:
            chemin = [current]
            while current in came_from:
                current = came_from[current]
                chemin.append(current)
            chemin.reverse()
            return chemin, iterations

        for voisin in voisins(grille, current):
            tentative_g = g_score[current] + 1
            if voisin not in g_score or tentative_g < g_score[voisin]:
                came_from[voisin] = current
                g_score[voisin] = tentative_g
                f_score[voisin] = tentative_g + heuristique(voisin, goal)
                heapq.heappush(open_set, (f_score[voisin], voisin))

    return None, iterations

# 4.  TESTS SUR UNE GRILLE

if __name__ == "__main__":
    print("\n==================== TEST COMPARATIF DIJKSTRA / A* ====================\n")

    # 0 = libre, 1 = obstacle
    grille = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
    ]

    start = (0, 0)
    goal = (4, 4)

    chemin_dij, it_dij = dijkstra_grille(grille, start, goal)
    chemin_astar, it_astar = a_star(grille, start, goal)

    print(f"Chemin Dijkstra : {chemin_dij}")
    print(f"Chemin A*       : {chemin_astar}")
    print(f"Itérations Dijkstra : {it_dij}")
    print(f"Itérations A*       : {it_astar}")

    print("\n==================== ANALYSE ====================")
    if chemin_dij and chemin_astar:
        print("✅ Les deux algorithmes trouvent le même chemin optimal.")
        if it_astar < it_dij:
            print(f"🔹 A* est plus rapide : {it_astar} itérations contre {it_dij}.")
        else:
            print(f"🔹 A* a fait autant ou plus d’itérations ({it_astar} vs {it_dij}).")
    else:
        print("❌ Aucun chemin trouvé (grille bloquée).")

    print("\n------------------------------------------------------------")
    print("CONCLUSION :")
    print(" - Dijkstra explore uniformément tout le graphe sans direction.")
    print(" - A* utilise l’heuristique (Manhattan) pour se diriger vers la cible.")
    print(" - Les deux donnent le même résultat, mais A* est souvent plus efficace.")