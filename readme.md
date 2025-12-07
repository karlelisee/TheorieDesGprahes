# Rapport – Mise en œuvre d’Algorithmes de Graphes  
École Hexagone – 2025

Ce projet a pour objectif d’implémenter et d’étudier plusieurs algorithmes fondamentaux en théorie des graphes. Les exercices proposés couvrent l’exploration de graphes, l’analyse d’accessibilité, le calcul de plus courts chemins et l’étude comparative de différentes méthodes de recherche. L’ensemble des algorithmes a été implémenté en Python, et testés sur différents graphes issus des Travaux Dirigés.

---

## 1. Parcours en profondeur d’un graphe (DFS)

Le premier exercice consiste à coder l’algorithme de parcours en profondeur (Depth First Search) à l’aide d’une pile. L’objectif est d’explorer le graphe en suivant systématiquement un chemin jusqu’à atteindre une impasse, puis de revenir en arrière pour explorer les autres branches.

Le graphe utilisé pour les tests est celui de l’exercice 2 du TD_Graphe_1. L’algorithme marque le sommet de départ, l’empile, puis inspecte le sommet au sommet de la pile. S’il existe un voisin non visité, celui-ci est visité immédiatement ; sinon, le sommet est dépilé.

L’exécution montre clairement la progression du parcours ainsi que les retours arrière. L’ordre final obtenu dans notre cas est :

**A → B → D → E → F → C**

ce qui confirme que l’algorithme explore d’abord en profondeur, avant de revenir en arrière lorsque nécessaire.

---

## 2. Fermeture transitive : Algorithme de Roy–Warshall

Le second exercice porte sur la fermeture transitive d’un graphe orienté à l’aide de l’algorithme de Roy–Warshall, utilisant une matrice d’adjacence. L’objectif est de déterminer, pour chaque paire de sommets, s’il existe un chemin permettant d’aller de l’un à l’autre.

L’algorithme repose sur l’idée qu’un sommet intermédiaire \(k\) peut créer une nouvelle accessibilité entre \(i\) et \(j\). À chaque itération, la matrice est mise à jour selon la règle :

\[
M[i][j] = M[i][j] \;\lor\; (M[i][k] \land M[k][j]).
\]

Trois graphes ont été testés : G1, G2 et G3 (exercice 7 du TD). Les matrices intermédiaires ont été affichées à chaque itération, ce qui permet d’observer l’évolution progressive de l’accessibilité.

Une comparaison importante concerne les graphes G1 et G2. L’étude des fermetures transitives montre clairement que :

**G1 et G2 ne sont pas τ-équivalents**,  
car ils ne possèdent pas la même closure, malgré des structures initiales similaires.

---

## 3. Chemins optimaux dans un graphe pondéré

### 3A — Algorithme de Dijkstra

Le troisième exercice concerne la recherche de chemins minimaux dans un graphe pondéré à poids positifs. L’algorithme de Dijkstra a été implémenté à l’aide d’une file de priorité pour sélectionner le sommet non traité ayant la plus petite distance courante.

Le graphe de test provient du TD Chemins Optimaux 1. L’exécution depuis le sommet x1 permet de calculer les distances minimales vers tous les autres sommets. Le plus court chemin retrouvé pour atteindre x6 est :

**x1 → x2 → x4 → x6**,  
avec une distance totale de **6**, parfaitement conforme au résultat attendu.

### 3B — Algorithme A* appliqué à une grille

L’exercice suivant étudie l’algorithme A*, appliqué cette fois à une grille comportant des obstacles. Une heuristique de Manhattan est utilisée :

\[
h(x, y) = |x_1 - x_2| + |y_1 - y_2|.
\]

Deux algorithmes ont été comparés : **Dijkstra** (sans heuristique) et **A*** (avec heuristique), afin d’observer l'amélioration de performance apportée par l’estimation de la distance restante vers l’objectif.

Les deux algorithmes trouvent le même chemin optimal, mais le nombre d’itérations diffère fortement : A* explore beaucoup moins d’états, ce qui confirme son efficacité dans les problèmes de navigation en grille.

---

## 4. Chemins optimaux tous couples : Algorithme de Floyd–Warshall

Le dernier exercice consiste à implémenter l’algorithme de Floyd–Warshall, permettant de calculer l’ensemble des plus courts chemins entre toutes les paires de sommets d’un graphe pondéré. L’algorithme fonctionne même en présence de poids négatifs, à condition qu’il n’y ait pas de cycle négatif.

À chaque itération, le sommet intermédiaire \(k\) est utilisé pour améliorer potentiellement la distance entre les sommets \(i\) et \(j\). L’algorithme met aussi à jour une matrice de prédécesseurs pour reconstituer les chemins complets.

Les tests ont été effectués sur un graphe pondéré issu du TD Chemins Optimaux 2. L’algorithme calcule correctement la matrice finale des distances minimales ainsi que les chemins associés. Par exemple, pour aller du sommet A au sommet E, l’algorithme reconstitue le chemin optimal, confirmant la cohérence du modèle.

---

## Conclusion générale

Ce projet couvre trois grands domaines de la théorie des graphes :

- **l’exploration** (DFS),  
- **l’accessibilité** (Roy–Warshall),  
- **l’optimisation** (Dijkstra, A*, Floyd–Warshall).

Les algorithmes ont été codés, testés et analysés sur plusieurs graphes représentatifs.  
Les résultats obtenus sont conformes aux attentes des TPs et illustrent les différences structurelles entre les algorithmes : Dijkstra explore uniformément, A* exploite une heuristique, Floyd–Warshall procède par programmation dynamique, et Roy–Warshall par mise à jour booléenne.

Ce travail permet de mieux comprendre les forces, les limites et les domaines d’application de chaque algorithme, tout en consolidant la maîtrise des représentations de graphes et des méthodes de parcours.

---
