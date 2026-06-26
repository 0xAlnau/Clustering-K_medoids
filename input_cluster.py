import csv
from Lloc import *
from cluster_k_medoids import *

llocs = []
n = 0
k = 0

print("Com vols introduir les dades al programa?")
print("1 - Per terminal")
print("2 - Amb un arxiu .csv")
resposta = input("Introduiex 1 o 2: ")
resposta = int(resposta)

if (resposta == 1):
    n = input("Quants llocs vols posar? ")
    n = int(n)
    k = input("Quants clústers vols? ")
    k = int(k)

    for i in range(0, n):
        print(f"- Lloc[{i}]")
        nom = input("       Nom: ")
        x = input("     Coordenada x: ")
        y = input("     Coordenada y: ")
        llocs.append(Lloc(nom,x,y))

else:
    arxiu = input("Indica el nom de l'arxiu (de la carpeta Inputs-CSV i amb el .csv): ")
    with open("Inputs-CSV/" + arxiu) as f:
        dades = csv.DictReader(f)
        i = 0
        for row in dades:
            nom = row["NomLloc"]
            x = row["Coordenada X"]
            y = row["Coordenada Y"]
            llocs.append(Lloc(nom,x,y))
            if (i == 0):
                k = int(row["Clusters"])
            i = i + 1
        n = i

clustering = Clustering(llocs, n, k)
clustering.compute()
clustering.show_results()

