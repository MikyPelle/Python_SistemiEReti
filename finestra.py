import pygame
import sys

pygame.init()

# Inizializza lo schermo
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visualizzazione Punteggio")

# Carica le immagini dei numeri
punti_unita = [pygame.image.load('sprites/0.png').convert_alpha(),
               pygame.image.load('sprites/1.png').convert_alpha(),
               pygame.image.load('sprites/2.png').convert_alpha(),
               pygame.image.load('sprites/3.png').convert_alpha(),
               pygame.image.load('sprites/4.png').convert_alpha(),
               pygame.image.load('sprites/5.png').convert_alpha(),
               pygame.image.load('sprites/6.png').convert_alpha(),
               pygame.image.load('sprites/7.png').convert_alpha(),
               pygame.image.load('sprites/8.png').convert_alpha(),
               pygame.image.load('sprites/9.png').convert_alpha()]
punti_decine = punti_unita
punti_centinaia = punti_unita

# Funzione per visualizzare il punteggio
def visualizza_punteggio(punteggio):
    # Estrai le cifre del punteggio
    centinaia = punteggio // 100
    decine = (punteggio % 100) // 10
    unita = punteggio % 10

    # Disegna le cifre sullo schermo
    screen.blit(punti_centinaia[centinaia], (100, 100))
    screen.blit(punti_decine[decine], (150, 100))
    screen.blit(punti_unita[unita], (200, 100))

# Esempio di utilizzo
punteggio = 1
visualizza_punteggio(punteggio)

# Aggiorna lo schermo
pygame.display.update()

# Loop principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()