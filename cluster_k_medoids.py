from math import sqrt
import matplotlib.pyplot as plt #cal fer pip install matplotlib
import random

class Clustering():
    def __init__(self, llocs, n, k):
        self.llocs = llocs
        self.n = n
        self.k = k
        self.clusters = []
        self.cost_global = 0
        self.medoids = []
        self.dist = [[-1] * n for _ in range(n)] #matriu NxN iniciada amb 0s


    #calcula la distancia euclidea entre dos llocs
    def euclidean_dist(self, p1, p2):
        dist = sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
        return dist


    #calcula les distancies entre tots els llocs
    def calc_distances(self):
        n = self.n
        llocs = self.llocs

        for i in range(n):
            for j in range(n):
                if self.dist[i][j] == -1: #si no esta ja calculat
                    self.dist[i][j] = self.euclidean_dist(llocs[i], llocs[j])
                    self.dist[j][i] = self.dist[i][j]


    #calcula els medoids inicials de forma aleatoria
    def calc_medoids(self):
        #                            0..n           escull k
        self.medoids = random.sample(range(self.n), self.k)


    #retorna true si el valor per parametre no es als medoids
    def not_in_medoids(self, i):
        for e in self.medoids:
            if i == e:
                return False
        return True


    #associa cada lloc al medoid més proper
    def associa_llocs(self):
        n = self.n
        k = self.k
        llocs = self.llocs

        self.clusters = [[] for _ in range(k)] #crea k llistes buides
        self.cost_global = 0 #tornem a iniciar a 0

        for j in range(k): #posem a cada cluster el medoid corresponent
            idx = self.medoids[j]
            self.clusters[j].append(llocs[idx])

        for i in range(n): #mirem cada lloc
            p = llocs[i]
            m = -1
            dist = float('inf') #infinit
            for j in range(k): #mirem amb qui esta mes aprop
                l = self.medoids[j]
                if self.not_in_medoids(i) and self.dist[i][l] < dist:
                    dist = self.dist[i][l]
                    m = j

            if m != -1: #nomes afegim si no es un medoid
                self.clusters[m].append(p)
                self.cost_global = self.cost_global + dist



    #crea els clústers
    def compute(self):
        n = self.n
        k = self.k

        self.calc_distances()
        self.calc_medoids()
        self.associa_llocs()

        #anem provant combinacions canviant medoids
        millora = True
        while millora:
            m_best = -1 #millor medoid a intercanviar
            o_best = -1 #millor no medoid a intercanviar
            millora = False #forcem a intentar millorar
            millor_cost_act = self.cost_global

            for l in range(k):
                i = self.medoids[l]
                for j in range(n):
                    if self.not_in_medoids(j):
                        self.medoids[l] = j
                        self.associa_llocs()

                        if self.cost_global < millor_cost_act:
                            millor_cost_act = self.cost_global
                            m_best = l
                            o_best = j
                            millora = True
                        self.medoids[l] = i

            if millora:
                self.medoids[m_best] = o_best
                self.associa_llocs()
            else:
                self.associa_llocs()


    #mostra els clústers per terminal
    def show_results(self):
        n = self.n
        k = self.k
        for i in range(k):
            print(f"\nCluster {i}:")
            m = len(self.clusters[i])
            for j in range(m):
                lloc = self.clusters[i][j]
                print(f"     · {lloc.nom}")


    #mostra els clusters de forma visual
    def plot_clusters(self):
        k = self.k
        colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow']

        plt.figure(figsize=(10, 7))

        for j in range(k):
            cluster_color = colors[j % len(colors)] #per si hi ha més clusters que colors

            x_vals = [lloc.x for lloc in self.clusters[j]] #extreiem coords
            y_vals = [lloc.y for lloc in self.clusters[j]]
            noms = [lloc.nom for lloc in self.clusters[j]]

            plt.scatter(x_vals, y_vals, c=cluster_color, alpha=0.5, s=60, label=f'Cluster {j}') #pintem punts normals

            for i, nom in enumerate(noms): #afegim els noms
                plt.annotate(nom, (x_vals[i], y_vals[i] + 0.15), fontsize=9, ha='center', alpha=0.8)

            medoid_idx = self.medoids[j] #marquem medoid
            medoid_lloc = self.llocs[medoid_idx]
            plt.scatter(medoid_lloc.x, medoid_lloc.y, c=cluster_color, edgecolors='black', marker='X', s=250)

        plt.title('Visualització K-medoids', fontsize=16, fontweight='bold') #configuracions finals
        plt.xlabel('Coordenada X')
        plt.ylabel('Coordenada Y')
        plt.grid(True, linestyle='--', alpha=0.4)

        plt.show()

