import sys
def sceltaNodo(non_visitati, label):
    min_label = sys.maxsize
    min_nodo = None
    for nodo in non_visitati:
        labelNodo = label[nodo]
        if labelNodo < min_label:
            min_label = labelNodo
            min_nodo = nodo
    return min_nodo
            
def dijkstra(nodo_sorg, mat):
    n_nodi = len(mat)
    non_visitati = set([i for i in range(0,n_nodi)])
    label = {i:sys.maxsize for i in range(0,n_nodi)}
    label[nodo_sorg] = 0
    print(label)
    while len(non_visitati) != 0:
        nodoCorrente = sceltaNodo(non_visitati,label)
        non_visitati.remove(nodoCorrente)
        for nodoVicino, peso in enumerate(mat[nodoCorrente]):
            if peso > 0:
                nuovaLabel = label[nodoCorrente] + peso
                if nuovaLabel < label[nodoVicino]:
                    label[nodoVicino] = nuovaLabel
    return label
    

def main():
    mat1=[[0,4,0],
          [4,0,3],
          [0,3,0]]
    
    label=dijkstra(1,mat1)
    print(label)

if __name__ == '__main__':
    main()