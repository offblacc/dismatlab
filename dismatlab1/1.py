from math import sqrt as sq
from numpy import linalg as l

if __name__ == '__main__':
    lambda1 = float(input("Unesite prvi koeficijent λ_1 rekurzivne relacije: "))  # != lambda iz zapisa opceg clana
    lambda2 = float(input("Unesite drugi koeficijent λ_2 rekurzivne relacije: "))
    a0 = float(input("Unesite vrijednost nultog clana niza a_0: "))
    a1 = float(input("Unesite vrijednost prvog clana niza a_1: "))
    n = int(input("Unesite redni broj n trazenog clana niza: "))

    # kvadratna: -b + -sqrt(b ** 4 - ac) / 2a
    # b: lambda1
    # a: -1
    # c: lambda2
    x1 = (-lambda1 + sq(lambda1 ** 2 - 4 * (-1) * lambda2)) / (2 * (-1))
    x2 = (-lambda1 - sq(lambda1 ** 2 - 4 * (-1) * lambda2)) / (2 * (-1))
    # lambda1*x1^n + n*lambda2*x2^n = an
    print(x1)
    print(x2)

    if x1 == x2:
        lambda_1 = a0
        lambda_2 = (a1 - lambda_1 * x1) / x2
        print("Vrijednost n-tog clana niza pomocu formule: " + str(lambda_1 * x1 ** n + n * lambda_2 * x2 ** n))
    else:
        lambda_1 = l.det([[a0, x2 ** 0], [a1, x2]]) / l.det([[x1 ** 0, x2 ** 0], [x1, x2]])
        lambda_2 = l.det([[x1 ** 0, a0], [x1, x2]]) / l.det([[x1 ** 0, x2 ** 0], [x1, x2]])
        print("else")
        print(lambda_1)
        print(lambda_2)
        print("Vrijednost n-tog clana niza pomocu formule: " + str(lambda_1 * x1 ** n + lambda_2 * x2 ** n))

    # rekurzivno
    medurezultati = dict()


    def rek(n):
        if n == 0:
            return a0
        elif n == 1:
            return a1
        else:
            if n not in medurezultati.keys():
                medurezultati.update({n: lambda1 * rek(n - 1) + lambda2 * rek(n - 2)})
            return medurezultati.get(n)


    print("Vrijednost n-tog clana niza iz rekurzije: " + str(rek(n)))
