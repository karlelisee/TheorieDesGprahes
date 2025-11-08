"""
TP Graphe – Exercice 1° : Parcours en profondeur (DFS)
"""

graphe = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graphe, sommet_depart):
    """
    Implémente l'algorithme de parcours en profondeur à l'aide d'une pile.
    """
    pile = []              # Pile pour gérer les sommets à visiter
    visites = []           # Liste des sommets visités dans l’ordre

    # Étape initiale
    pile.append(sommet_depart)
    visites.append(sommet_depart)

    print(f"Départ du parcours en profondeur depuis : {sommet_depart}\n")

    while pile:
        sommet = pile[-1]  # Sommet en haut de la pile
        print(f"Sommet courant : {sommet} | Pile : {pile}")

        # Chercher un voisin non visité
        voisin_non_visite = None
        for voisin in graphe[sommet]:
            if voisin not in visites:
                voisin_non_visite = voisin
                break

        # Si un voisin non visité existe, on le marque et on l’empile
        if voisin_non_visite:
            print(f"→ Visite du voisin : {voisin_non_visite}")
            visites.append(voisin_non_visite)
            pile.append(voisin_non_visite)
        else:
            # Aucun voisin non visité : on dépile
            print(f"← Retour arrière depuis {sommet}")
            pile.pop()

    print("\nParcours terminé.")
    print("Sommets visités dans l’ordre :", visites)
    return visites

# Exécution
ordre = dfs(graphe, 'A')
print("\nOrdre final de parcours :", ordre)
