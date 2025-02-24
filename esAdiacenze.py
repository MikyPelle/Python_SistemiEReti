import networkx as nx
import matplotlib.pyplot as plt

def mat_to_diz(adiacenze):
    diz = {chiave: [] for chiave in range(len(adiacenze))}
    for i in range(len(adiacenze)):
        for j in range(len(adiacenze[i])):
            if adiacenze[i][j] == 1:
                diz[i].append(j)
    return diz

def main():
    d = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}
    adiacenze = [[1 if j in d[i] else 0 for j in range(len(d))] for i in range(len(d))]
    
    G = nx.Graph()
    G.add_nodes_from(range(len(adiacenze)))

    for i in range(len(adiacenze)):
        for j in range(i + 1, len(adiacenze[i])):
            if adiacenze[i][j] == 1:
                G.add_edge(i, j)

    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

if __name__ == '__main__':
    main()