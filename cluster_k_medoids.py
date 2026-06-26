class Clustering():
    def __init__(self, llocs, n, k):
        self.llocs = llocs
        self.n = n
        self.k = k
        self.clusters = []

    def compute(self):
        n = self.n
        k = self.k
        div = n // k

        for i in range(0, k):
            self.clusters.append([self.llocs[i]])
            if (i == k - 1):
                for j in range(k, n):
                    self.clusters[i].append(self.llocs[j])

    def show_results(self):
        n = self.n
        k = self.k
        for i in range(0, k):
            print(f"Cluster {i}:")
            m = len(self.clusters[i])
            for j in range(0, m):
                lloc = self.clusters[i][j]
                print(f"     · {lloc.nom}")

