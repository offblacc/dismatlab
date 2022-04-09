from __future__ import print_function  # python3 style print (for easier printing of distances)
from itertools import permutations

"""
Run with python2.7/pypy (using pypy for faster execution and more efficient memory usage)
"""


# -------------------------------- functions -----------------------------

def tezina_brida(k, l):  # parametar k i parametar l su indexi vrhova koje brid spaja
    """
    :param k: vrh manjeg indeksa
    :param l: vrh veceg indeksa
    :return: type int
    """
    if k > l:
        raise Exception("param k must be < l")
    return (a * k + b * l) ** 2 + 1


# -------------------------------- classes -------------------------------
class Graph:
    def __init__(self, n, a, b):
        """
        Popuni n*n matricu 'distances' duljinama bridova gdje su indexi vrhovi. Parametar n je dimenzija matrice dok
        su a i b konstante koje se koriste prilikom racunanja distance izmedu vrhova. Popuni array visited_vertecies
        bool vrijednostima False, jer su u pocetku svi vrhovi jos neposjeceni.
        :param n: Dimenzija matrice
        :param a: Parametar a type int
        :param b: Parametar b type int
        """
        self.n, self.a, self.b = n, a, b
        self.distances = [[tezina_brida(min(k, l), max(k, l)) if k != l else 0 for k in range(1, n + 1)] for l in
                          range(1, n + 1)]
        self.visited_vertecies = [False for _ in range(self.n)]
        self.visited_edges = [[False for _ in range(self.n)] for _ in range(self.n)]

    def get_min_edge(self):
        """
        Nalazi najmanji brid na cijelom grafu.
        :return: Tuple: (duljina_najmanjeg_brida, jedan njemu incidentan vrh, drugi njemu incidentan vrh)
        """
        global_min = (float('inf'), None, None)  # None, None su vrhovi za taj dist
        for i in range(self.n):
            min = (float('inf'), None, None)
            for j in range(self.n):
                if self.distances[i][j] != 0 and self.distances[i][j] < min[0]:
                    min = (self.distances[i][j], i, j)
            if min[0] < global_min[0]:
                global_min = min
        return global_min  # (min_brid, tocka1, tocka2)

    def print_distances(self):
        """
        Ispise n*n matricu duljina bridova.
        """
        for row in self.distances:
            for x in row:
                print(str(x) + str(" "), end="")
            print()

    def all_points_visited(self):
        """
        Provjerava jesu li svi vrhovi posjeceni -> gotov ciklus
        :return: bool
        """
        for visited in self.visited_vertecies:
            if not visited:
                return False
        return True

    def pohlepni(self, point1, point2, first_call):
        if first_call:
            return graph.distances[point1][point2] + self.pohlepni(graph.get_min_edge()[1], graph.get_min_edge()[2],
                                                                   False)
        graph.visited_vertecies[point1] = True
        graph.visited_vertecies[point2] = True
        if graph.all_points_visited():  # ako smo sve obisli, spoji ih
            return graph.distances[point1][point2]
        min_dist = float('inf')
        inx_min = None
        vrh_s_manjim_incidentnim_bridom = None
        # looking from point 1
        avail = graph.distances[point1]
        for i in range(len(avail)):
            if 0 != avail[i] <= min_dist and not graph.visited_vertecies[i]:
                min_dist = avail[i]
                inx_min = i
                vrh_s_manjim_incidentnim_bridom = 1
        # looking from point 2
        avail = graph.distances[point2]
        for i in range(len(avail)):
            if 0 != avail[i] <= min_dist and not graph.visited_vertecies[i]:
                min_dist = avail[i]
                inx_min = i
                vrh_s_manjim_incidentnim_bridom = 2
        if vrh_s_manjim_incidentnim_bridom is not None:
            if vrh_s_manjim_incidentnim_bridom == 1:
                point1 = inx_min
            elif vrh_s_manjim_incidentnim_bridom == 2:
                point2 = inx_min

            return min_dist + self.pohlepni(point1, point2, False)
        # ako nisu svi posjeceni vrati trenutnu duljinu + pohlepni za novi vrh

    def reset_visited(self):
        """
        Postavlja matricu posjecenih vrhova na False, npr. pripremajuci objekt klase Graph za novo trazenje ciklusa.
        """
        for i in range(len(self.visited_vertecies)):
            self.visited_vertecies[i] = False

    def iscrpni(self):
        """
        Prolazi sve permutacije vrhova odnosno sve moguce cikluse + povratak na prvi vrh i vraca najkraci put.
        Brute force pristup. Neizbjezna vremenska slozenost O(n!), linearna prostorna slozenost.
        :return: int: minimum distance, best solution to the salesman problem
        """
        self.reset_visited()
        niz = list(range(self.n))
        min_dist = float('inf')
        for perm in permutations(niz):
            dist = 0
            for i in range(self.n - 1):
                dist += self.distances[perm[i]][perm[i + 1]]
            dist += self.distances[perm[-1]][perm[0]]
            if dist < min_dist:
                min_dist = dist
        self.reset_visited()
        return min_dist


# --------------------------------- input --------------------------------
n, a, b = map(int, raw_input("Unesite redom, odvojene razmakom, parametre n, a i b: ").split())
graph = Graph(n, a, b)
graph.print_distances()
pohlepni = graph.pohlepni(graph.get_min_edge()[1], graph.get_min_edge()[2], True)
print("Pohlepni algoritam nalazi ciklus duljine " + str(pohlepni))
iscrpni = graph.iscrpni()
print("Iscrpni algoritam nalazi ciklus duljine " + str(iscrpni))
if iscrpni == pohlepni:
    print("Pohlepni algoritam daje optimalno rjesenje")
else:
    print("Pohlepni algoritam ne daje optimalno rjesenje")
