import copy
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from samplegraph import SampleGraph


sample_graph = SampleGraph(5, 90, 900, 43)
sample_graph.draw_graph()

class Dijkstra:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.path = copy.copy(self.graph.graph)
        self.keys = list(self.path.keys())
        self.start = start
        self.end = end
        self.actual_path = [self.start]


    def fit(self):

        if self.path[self.start][self.keys.index(self.end)] != np.inf:
            self.actual_path.append(self.end)
        else:
            for i in range(len(self.keys)):
                current = np.argmin(self.path[self.actual_path[-1]])
                self.actual_path.append(self.keys[current])

                if self.actual_path[-1] == self.end:
                    break

                for up in self.actual_path[:-1]:
                    self.path[self.actual_path[-1]][self.keys.index(up)] = np.inf

        print(self.actual_path)

    def draw_path(self):
        keys = list(self.path.keys())
        G = nx.Graph()

        for i in range(len(self.actual_path) - 1):
            u = self.actual_path[i]
            v = self.actual_path[i + 1]
            weight = self.graph.graph[u][keys.index(v)]
            if weight != np.inf:
                G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G, seed=43)
        nx.draw(G, pos, with_labels=True, node_color="yellow", node_size=1500, font_size=10, font_weight="bold")
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()


dijkstra = Dijkstra(sample_graph, "LMA", "OTL")
dijkstra.fit()
dijkstra.draw_path()