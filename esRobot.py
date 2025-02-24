import pygame
import sys
from pygame.locals import *

def calc_pav():
    with open("mappa.csv", "r") as f:
        mat = [[int(c) for c in riga.split(", ")] for riga in f.readlines()]
    return mat

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
    lato_x = 100
    lato_y = 100
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    matrice = [[-1 for _ in range(n_x)] for _ in range(n_y)]
    k = 1

    #SETUP per schermo, immagini e font
    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x , n_y * lato_y))
    strada = pygame.image.load("pavimento.png")
    strada = pygame.transform.scale(strada, (lato_x, lato_y))
    muro = pygame.image.load("muro.png")
    muro = pygame.transform.scale(muro, (lato_x, lato_y))
    robot = pygame.image.load("robot.png")
    robot = pygame.transform.scale(robot, (lato_x, lato_y))
    font = pygame.font.SysFont("Verdana", 18) 
    
    for riga in pavimento:
        for casella in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            text = font.render(f"{k}", True, (0,0,0))
            if casella == 1:
                surf1.blit(muro, (0, 0))
                screen.blit(surf1, (lato_x-100, lato_y-100))  
            elif casella == 0:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x-20, lato_y-80))  
                screen.blit(surf1, (lato_x-100, lato_y-100))  
                screen.blit(text, text_pos)
                k += 1
            elif casella == 3:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x-20, lato_y-80))  
                screen.blit(surf1, (lato_x-100, lato_y-100))
                screen.blit(robot, (lato_x-100, lato_y-100)) 
                screen.blit(text, text_pos)
                k += 1
            
            pygame.display.flip()
            lato_x += 100
            
        lato_x = 100
        lato_y += 100

        #screen.blit(robot, (0, 0))
    k = 1
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0 or casella == 3:
                matrice[indice_riga][indice_colonna] = k
                k += 1
    
    diz = {}
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            adiacenze = []
            if casella == 0 or casella == 3:
                if indice_riga > 0:
                    if matrice[indice_riga-1][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga-1][indice_colonna])
                if indice_colonna > 0:
                    if matrice[indice_riga][indice_colonna-1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna-1])
                if indice_riga < n_y-1:
                    if matrice[indice_riga + 1][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga+1][indice_colonna])
                if indice_colonna < n_x - 1:
                    if matrice[indice_riga][indice_colonna + 1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna+1])
                    diz[matrice[indice_riga][indice_colonna]] = adiacenze
    
    print(diz)  
    lista_n = []
    for indice_riga, riga in enumerate(matrice):
        for indice_colonna, n in enumerate(riga):
            if n != -1:
                lista_n.append(matrice[indice_riga][indice_colonna])
    print(lista_n)

    #pygame.quit()
    #exit()
    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
    pygame.quit()

if __name__ == "__main__":
    main()