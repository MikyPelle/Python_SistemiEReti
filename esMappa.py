import pygame

def draw_map(screen, mappa, lato_quad, pavimento, muro, font):
    k = 0
    for y, row in enumerate(mappa):
        for x, cell in enumerate(row):
            if cell == 1:
                screen.blit(muro, (x * lato_quad, y * lato_quad))
            else:
                screen.blit(pavimento, (x * lato_quad, y * lato_quad))
                testo = font.render(f"{k}", True, (0, 0, 0))
                text_rect = testo.get_rect(center=(x * lato_quad + lato_quad - 15, y * lato_quad + 15))
                screen.blit(testo, text_rect)
                k += 1
def findFreeCell(mat):
    pass
    
               
def main():
    pygame.init()
    lato_quad = 100
    mappa = []

    pavimento = pygame.image.load("pavimento.png")
    pavimento = pygame.transform.scale(pavimento, (lato_quad, lato_quad))
    muro = pygame.image.load("muro.png")
    muro = pygame.transform.scale(muro, (lato_quad, lato_quad))
    robot = pygame.image.load("robot.png")
    robot = pygame.transform.scale(robot, (lato_quad, lato_quad))
    
    with open("mappa.csv", "r") as f:
        for riga in f.readlines():
            riga = riga.split(',')  
            riga_int = [int(c) for c in riga]
            mappa.append(riga_int)
    
    n_x = len(mappa[0])
    n_y = len(mappa)
    screen_width = n_x * lato_quad
    screen_height = n_y * lato_quad
    mat = [[-1 for _ in range(n_y)] for _ in range(n_x)]
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.SysFont(None, 30)
    
    k=0
    for indice_riga, riga in enumerate(mappa):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0 or casella == 3:
                mat[indice_riga][indice_colonna] = k
                k += 1

    diz = {}
    adiacenze = []
    for indice_riga, riga in enumerate(mappa):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0 or casella == 3:
                if indice_riga != 0: #tocca il soffitto (controllo tutti tranne soffitto)
                    if mat[indice_riga - 1 ][indice_colonna] != -1:
                        adiacenze.append(mat[indice_riga-1][indice_colonna])
                if indice_riga != n_y - 1: #tocca parete sotto 
                    if mat[indice_riga + 1][indice_colonna] != -1:
                        adiacenze.append(mat[indice_riga+1][indice_colonna])   
                if indice_colonna != 0: #tocca sinistra
                    if mat[indice_riga][indice_colonna - 1] != -1:
                        adiacenze.append(mat[indice_riga][indice_colonna-1])
                if indice_colonna != n_x - 1: #tocca destra 
                    if mat[indice_riga][indice_colonna + 1] != -1:
                        adiacenze.append(mat[indice_riga][indice_colonna+1])               
                diz[mat[indice_riga][indice_colonna]] = adiacenze
                adiacenze = []

    print(mat)
    print(diz)
    
    pygame.display.set_caption('Mappa')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_map(screen, mappa, lato_quad, pavimento, muro, font)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
