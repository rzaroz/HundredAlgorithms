import string
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class SampleGraph:

    def __init__(self, vertex: int, random_blocked: int, weight_range: int, random_seed): # Random blocked paths created in the graph based on percentage
        random.seed(random_seed)
        self.vertex = vertex
        self.weight_range = weight_range
        self.random_blocked = self.vertex * random_blocked // 100
        names = self.generate_unique_names()
        self.graph = {name: np.full(self.vertex, np.inf) for name in names}
        self.create_adjacency_matrix()
        self.block_path()

    def create_adjacency_matrix(self):
        for i, k in enumerate(self.graph.keys()):
            for v in range(self.vertex):
                if i != v:
                    if self.graph[k][v] == np.inf:
                        random_weight = random.randint(1, self.weight_range)
                        self.graph[k][v] = random_weight
                        self.graph[list(self.graph.keys())[v]][i] = random_weight

    def generate_unique_names(self):
        names = set()
        while len(names) < self.vertex:
            name = ''.join(random.choices(string.ascii_uppercase, k=3))
            names.add(name)
        return list(names)

    def block_path(self):
        for blocked in range(self.random_blocked):
            keys = list(self.graph.keys())
            choises = random.choices(keys, k=2)
            self.graph[choises[0]][keys.index(choises[1])] = np.inf
            self.graph[choises[1]][keys.index(choises[0])] = np.inf

    def draw_graph(self):
        keys = list(self.graph.keys())
        G = nx.Graph()

        for i, k in enumerate(keys):
            for j, w in enumerate(self.graph[k]):
                if w != np.inf:
                    G.add_edge(k, keys[j], weight=w)

        pos = nx.spring_layout(G, seed=43)
        nx.draw(G, pos, with_labels=True, node_color="yellow", node_size=1500, font_size=10, font_weight="bold")
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

if __name__ == "__main__":
    sample = SampleGraph(5, 90, 900, 43)
    sample.draw_graph()