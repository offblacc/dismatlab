from builtins import FileNotFoundError


# noinspection PyPep8Naming,PyShadowingNames
class Graph:
    def __init__(self, nodes, S):
        self.nodes = nodes
        self.S = S
        self.graph = [[abs(i - j) in self.S and i != j for j in range(1, nodes + 1)] for i in range(1, nodes + 1)]

    def can_colour_node_with(self, vrh, colors, c):
        for i in range(self.nodes):
            if self.graph[vrh][i] and colors[i] == c:  # njegov susjedni je obojan istom bojom, vrati false
                return False
        return True  # ne postoji susjedni obojan istom bojom, mozemo obojati vrh 'vrh' bojom c

    def try_coloring_graph(self, m, colors, vrh=0):
        """
        Rekurzivno traži je li moguće obojati graf sa m boja.

        :param m: Broj boja kojima pokušavamo obojati graf.
        :param colors: Lista boja obojanih vrhova, brojevi od 1 (do m). Korespondira indeksima vrhova (n-ta boja = boja
        n-tog vrha).
        :param vrh: Vrh koji trenutno pokušavamo obojati nekom od boja.
        :return: False/kromatski broj. True se vraća ali uvijek se samo interno obradi i vrati kromatski broj. False
        vraća ako kromatski broj nije pronađen odnosno potrebno je više od m boja za obojati graf.
        """
        if vrh == self.nodes:  # ako su svi vrhovi obojani
            # print(max(colors))  # rjesenje se moglo i odavde dobiti ali se izvuce na isti nacin nakon return True
            return True

        for c in range(1, m + 1):  # boje su indeksirane od 1, pokusavamo obojati sa m boja
            if self.can_colour_node_with(vrh, colors, c):  # nademo boju kojom smijemo obojati trenutni vrh
                colors[vrh] = c
                if self.try_coloring_graph(m, colors, vrh + 1):
                    return max(colors)  # ako je if vratio true pronaden je krom. broj i on je jednak 'najvecoj boji'
        return False  # ni jedno bojanje nije uspjelo, premalo boja

    # 'predfunkcija' - moram negdje prije rekurzivne funkcije a van glavnog programa inicijalizirati listu boja
    def kromatski_broj(self):
        """
        'Predfunkcija', samo inicijalizira colors i zove funkciju koja je rekurzivna. To je napravljeno zato što u
        prvom rekurzivnom pozivu trebam praznu listu boja - logički gledano to ostvarujem kao broj vrhova puta nula u
        listi. Mogu staviti defaultnu vrijednost u parametre funkcije, no budući da ovdje ona ovisi o broju vrhova nije
        moguće napraviti funkciju sa općenitom defaultnom vrijednosti. Za razliku od te liste vrh u prvom pozivu
        rekurzije treba biti nula što je konstantna vrijednost i ne ovisi ni o čemu pa ovdje u pozivu rekurzije
        izostavljamo taj argument. Funkcija počinje od broja 2 i ako njime ne možemo obojati graf pokušamo s 3 i tako
        dok ne nađemo neki kojim možemo obojati graf - to je kromatski broj.

        :return: int: Vraća kromatski broj.
        """
        i = 2
        found = self.try_coloring_graph(i, [0] * self.nodes)
        while not found:
            i += 1
            colors = [0] * self.nodes  # init listu boja
            found = self.try_coloring_graph(i, colors)
        return found

    def print_graph(self):
        for linija in self.graph:
            print([1 if x else 0 for x in linija])


input_file = input("Unesite ime datoteke: ")
try:
    with open(input_file, "r") as f:
        n = int(f.readline())
        len_s = int(f.readline())
        S = list(map(int, f.readline().split()))
        if len_s != len(S):
            print(f"Invalid input: given length of S is {len_s}, given S is of length {len(S)}.")
            exit(1)
except FileNotFoundError:
    print(f"Datoteka '{input_file}' nije pronađena.")
    exit(0)

g = Graph(n, S)
krom_broj = g.kromatski_broj()
print(f"Kromatski broj zadanog grafa je {krom_broj}")
