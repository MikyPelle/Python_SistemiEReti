import pygame
from pygame.locals import *
from sys import maxsize
import time
import heapq

def dijkstra(graph, start_vertex):
    # Numero di vertici nel grafo
    V = len(graph)
    # Distanze iniziali impostate a infinito
    distances = [float('inf')] * V
    # Percorso per raggiungere ogni nodo
    path = [-1] * V
    # Imposta la distanza del nodo di partenza a 0
    distances[start_vertex] = 0
    # Coda di priorità (min heap)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_vertex))

    while priority_queue:
        # Estrae il nodo con la distanza minima dalla coda
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # I nodi possono essere spinti più volte con distanze diverse.
        # Dobbiamo processare solo l'estrazione con la distanza più breve
        if current_distance > distances[current_vertex]:
            continue

        # Esamina ogni adiacente di 'current_vertex'
        for neighbor in range(V):
            weight = graph[current_vertex][neighbor]
            if weight > 0:  # esiste un arco
                distance = current_distance + weight

                # Solo se trovato un percorso più breve al vicino attraverso il vertice corrente
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances, path

def get_path(path, target_vertex):
    if path[target_vertex] == -1:
        return []  # Non è raggiungibile

    # Ricostruzione del percorso seguendo i predecessori
    result_path = []
    current_vertex = target_vertex
    while current_vertex != -1:
        result_path.append(current_vertex)
        current_vertex = path[current_vertex]

    return result_path[::-1]

def calc_pav():
    with open("mappa.csv", "r") as f:
        mat = [[int(c) for c in riga.split(",")] for riga in f.readlines()]
    return mat

def get_input(dir_x, dir_y, casella_player, diz, indice_x, indice_y, matrice, robot, screen, strada, font):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dir_x = 1
        dir_y = 0
        nuova_c, indice_x, indice_y = muovi(casella_player, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada, font)
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dir_x = -1
        dir_y = 0
        nuova_c, indice_x, indice_y = muovi(casella_player, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada, font)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dir_x = 0
        dir_y = -1
        nuova_c, indice_x, indice_y = muovi(casella_player, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada, font)
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dir_x = 0
        dir_y = 1
        nuova_c, indice_x, indice_y = muovi(casella_player, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada, font)
    elif keys[pygame.K_g]:
        matrice_ad = diz_to_mat(diz)
        sorg = 0
        #label, pred = dijkstra(sorg, matrice_ad)
        #print(label, pred)
        dest = 41  
        distances, path = dijkstra(matrice_ad, 0)
        final_path = get_path(path, dest)
        nuova_c = dest + 1
        #print(final_path)
        muovi_dijkstra(final_path, matrice, robot, screen, strada, font)
    else:
        dir_x = 0
        dir_y = 0
        nuova_c = casella_player
    return nuova_c, indice_x, indice_y


def muovi(casella_p, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada, font):


    nuova_casella = matrice[indice_y+dir_y][indice_x+dir_x]
    print(nuova_casella)
    lato_x_prec = (indice_x) * 100
    lato_y_prec = (indice_y) * 100
    lato_x = (indice_x + dir_x) * 100
    lato_y = (indice_y + dir_y) * 100
    print(lato_x, lato_y)
    if(nuova_casella in diz[casella_p]):
        #print("puo muovere")
        text = font.render(f"{matrice[indice_x][indice_y]}", True, (0,0,0))
        text_pos = text.get_rect(center=(lato_x_prec+80, lato_y_prec+20))
        surf1 = pygame.Surface((100, 100))
        surf1.blit(strada, (0, 0))
        #screen.blit(surf1, (lato_x, lato_y))
        screen.blit(surf1, (lato_x_prec, lato_y_prec))
        screen.blit(robot, (lato_x, lato_y))
        screen.blit(text, text_pos)
        pygame.display.flip()
        #print("fatto")
        indice_y = indice_y + dir_y
        indice_x = indice_x + dir_x
       

    '''surf1.blit(strada, (0, 0))
    text_pos = text.get_rect(center=(lato_x-20, lato_y-80))  
    screen.blit(surf1, (lato_x-100, lato_y-100))
    screen.blit(robot, (lato_x-100, lato_y-100)) 
    screen.blit(text, text_pos)'''
    return nuova_casella, indice_x, indice_y

def diz_to_mat(adj_dict):

    nodes = sorted(adj_dict.keys())
    node_index = {node: idx for idx, node in enumerate(nodes)}
    size = len(nodes)
    adjacency_matrix = [[0] * size for _ in range(size)]
    for node, neighbors in adj_dict.items():
        for neighbor in neighbors:
            adjacency_matrix[node_index[node]][node_index[neighbor]] = 1
            
    return adjacency_matrix

def muovi_dijkstra(percorso, matrice, robot, screen, strada, font):
    cont = 0
    while cont != len(percorso):
        for i_x, riga in enumerate(matrice):
            for i_y, colonna in enumerate(matrice[i_x]):
                if matrice[i_x][i_y] == (percorso[cont]+1):
                    #print(f"passa: {percorso[cont]+1}\n")
                    if(cont == 0):
                        cont += 1
                        pos_x = i_x * 100
                        pos_y = i_y * 100
                        break
                    else:   
                        cont += 1
                        pos_x_prec = pos_x
                        pos_y_prec = pos_y
                        pos_x = i_x * 100
                        pos_y = i_y * 100
                        text = font.render(f"{matrice[int(pos_x_prec/100)][int(pos_y_prec/100)]}", True, (0,0,0))
                        text_pos = text.get_rect(center=(int(pos_y_prec)+80, int(pos_x_prec)+20))
                        surf1 = pygame.Surface((100, 100))
                        surf1.blit(strada, (0, 0))
                        screen.blit(surf1, (pos_y_prec, pos_x_prec))
                        screen.blit(robot, (pos_y, pos_x))
                        screen.blit(text, text_pos)
                        time.sleep(0.4)
                        pygame.display.flip()
                        break
                


def main():

    lato_x = 100
    lato_y = 100
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    matrice = [[-1 for _ in range(n_x)] for _ in range(n_y)]
    k = 1

    casella_player = 0
    dir_x = 0
    dir_y = 0

    #SETUP per schermo, immagini e font
    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x , n_y * lato_y))
    muro = pygame.image.load("muro.png")
    muro = pygame.transform.scale(muro, (lato_x, lato_y))
    strada = pygame.image.load("pavimento.png")
    strada = pygame.transform.scale(strada, (lato_x, lato_y))
    robot = pygame.image.load("robot.png").convert_alpha()
    robot = pygame.transform.scale(robot, (lato_x, lato_y))
    font = pygame.font.SysFont("Verdana", 18) 
    
    for ind_y,riga in enumerate(pavimento):
        for ind_x, casella in enumerate(riga):
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
                casella_player = k
                indice_x = ind_x
                indice_y = ind_y
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

    k = 1
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0 or casella == 3:
                matrice[indice_riga][indice_colonna] = k
                k += 1

    diz = {}
    adiacenze = []
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0 or casella == 3:
                if indice_riga != 0: #tocca il soffitto (controllo tutti tranne soffitto)
                    if matrice[indice_riga - 1 ][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga-1][indice_colonna])
                if indice_riga != n_y - 1: #tocca parete sotto 
                    if matrice[indice_riga + 1][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga+1][indice_colonna])   
                if indice_colonna != 0: #tocca sinistra
                    if matrice[indice_riga][indice_colonna - 1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna-1])
                if indice_colonna != n_x - 1: #tocca destra 
                    if matrice[indice_riga][indice_colonna + 1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna+1])               
                diz[matrice[indice_riga][indice_colonna]] = adiacenze
                adiacenze = []
    
    print(diz)
    print(indice_x)
    print(indice_y)
    #print(matrice)

    #pygame.quit()
    #exit()
    done = False
    while not done:
        for ev in pygame.event.get():
            casella_player, indice_x, indice_y = get_input(dir_x, dir_y, casella_player, diz, indice_x, indice_y, matrice, robot, screen, strada, font)
            time.sleep(0.1)
            if ev.type == QUIT:
                done = True
    pygame.quit()

    '''#matrice_ad = diz_to_mat(diz)
    #print(matrice_ad)
    #time.sleep(3)
    sorg = 0
    #label, pred = dijkstra(sorg, matrice_ad)
    #print(label, pred)
    dest = 41  
    distances, path = dijkstra(matrice_ad, 0)
    final_path = get_path(path, 41)
    print(final_path)
    muovi_dijkstra(final_path, matrice, robot, screen, strada, font)'''

if __name__ == "__main__":
    main()